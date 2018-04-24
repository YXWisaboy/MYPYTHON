import numpy as np
import xlrd
import node
def mad_tree():
    nodex=headnode
    data=xlrd.open_workbook(r'去空后的计量表.xlsx')
    table=data.sheets()[0]
    rowc=table.nrows
    col=table.ncols
    for i in range(rowc):
        for j in range(col):
            a=table.row_values(i)[j]
            if a!='':
                flag=nodex.findchildnode(a)
                if flag==None:
                    nodec=node.node(a,nodex)
                    nodex.child.append(nodec)
                    if j==col-1:
                        headtable.append(nodec)
                nodex=nodex.findchildnode(a)
                nodex.count+=1
                #print(nodex.name,nodex.count)
        nodex=headnode
def print_ru(sup=0,con=0,sortf=0):
    lis=[]
    for i in headtable:
        if i.count>=sup:
            lis.append(i.name)
            node=i.parent
            num=float(i.count)/float(node.count)
            if num>=con:
                while node.name!='null':                    
                    #print(node.name)
                    lis.insert(0, node.name) 
                    node=node.parent
                fre.append((",".join(str(j) for j in lis),i.count,num))
        lis=[]
    #print(fre)
    y=[]
    if sortf==-1:
        y=fre
    if sortf==0:
        y=sorted(fre,key=lambda x:x[1],reverse=True)
    if sortf==1:
        y=sorted(fre,key=lambda x:x[2],reverse=True)    
    count=0
    File = open("hello2", "w")
    for x in y:
        if x[1]>=con:
            count+=1
            print(x)
            File.write(str(x) + "\n") 
        pass
    File.write(str(count) + "\n") 
    print(count)
    File.close()
        
headnode=node.node('null',None)
headtable=[]
fre=[]
mad_tree()
print_ru(3,con=0.8,sortf=0)