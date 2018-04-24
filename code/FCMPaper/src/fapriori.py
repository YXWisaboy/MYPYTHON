#coding=utf-8
from multiprocessing.dummy import list
import xlrd
from tensorflow.python.framework.dtypes import string
from builtins import str
def add_matix():    
    data=xlrd.open_workbook(r'分组准备表1.xlsx')
    dic={}
    table=data.sheets()[1]
    rowc=table.nrows
    for i in range(rowc):
        str1=table.row_values(i)[0].strip()
        dic[str1]=[]
        dic[str1].append(round(table.row_values(i)[1],2))
        dic[str1].append(round(table.row_values(i)[2],2))
        dic[str1].append(round(table.row_values(i)[3],2))
        #print(str,dic[str])
    table=data.sheets()[0]
    arr=[]
    name=[]
    x=table.row_values(0)[0]
    drgnum={}
    rowc=table.nrows
    for i in range(rowc+1):
        if i==rowc:
            arr.append(drgnum)
        else:    
            if table.row_values(i)[0]!=x:
                arr.append(drgnum)
                drgnum={}
                x=table.row_values(i)[0]

            name.append(table.row_values(i)[1]+'low('+str(dic[table.row_values(i)[1]][0])+')')
            name.append(table.row_values(i)[1]+'middle('+str(dic[table.row_values(i)[1]][1])+')')
            name.append(table.row_values(i)[1]+'high('+str(dic[table.row_values(i)[1]][2])+')')
            if table.row_values(i)[3]!=0:
                drgnum[table.row_values(i)[1]+'low('+str(dic[table.row_values(i)[1]][0])+')']=table.row_values(i)[3]
            if table.row_values(i)[4]!=0:
                drgnum[table.row_values(i)[1]+'middle('+str(dic[table.row_values(i)[1]][1])+')']=table.row_values(i)[4]
            if table.row_values(i)[5]!=0:
                drgnum[table.row_values(i)[1]+'high('+str(dic[table.row_values(i)[1]][2])+')']=table.row_values(i)[5]
    name = list(set(name))
    name1=[]
    for i in name:
        s=[]
        s.append(i)
        name1.append(s)
    return name1,arr
def makenext(a):
    List=[]
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            s=a[i]+a[j]
            s1 = list(set(s))
            if len(s1)==len(a[i])+1:
                flat=0
                for k in List:
                    if set(s1).issubset(k)==True:
                        flat=1
                if flat==0:
                    List.append(s1)
    return List
def findtime(data,li,sup,supli):
    numli=[]
    for i in li:
        sum=0
        for j in data:
            time=0;
            flag=0
            for c in i:
                if (c in j)==False:
                  flag=1
            if flag==0:
                time=1                
                for c in i:
                    time=time*j[c] 
            sum+=time     
        numli.append(sum)
    a=[]
    b=[]
    for i in range(len(li)):
        if numli[i]>=sup:
            a.append(li[i])
            b.append(numli[i])
            supli1=[]
            supli1.append(li[i])
            supli1.append(numli[i])
            supli.append(supli1)
    return a,b,supli

def findcer(bc,bd,c,d,cer,li):
    for i in range(len(c)):
        for j in range(len(bc)):
            if set(bc[j]).issubset(c[i])==True:
                newcer=d[i]/bd[j]
                if(newcer>=cer):
                    li1=[]
                    li1.append(bc[j])
                    li1.append(set(c[i]).difference(set(bc[j])))
                    li1.append(newcer)
                    li1.append(d[i])                    
                    li.append(li1)
    return li
#a=makenext([['b', 'a'], ['c', 'a'], ['b', 'c']])
'''
a=[['a'], ['b'], ['c']]
b=[{'a':0.2,'b':0.3,'c':0.5},{'a':0.8,'b':0.1,'c':0.1},{'b':0.5,'c':0.5}]
#a=list({'a', 'b'})
#print(c) 
#print(d)
'''
#按数组最后一列降序，输出
def printsult(a,str1):
    File = open(str1, "w")
    b=sorted(a,key=lambda x:x[-1],reverse=True)
    count=0
    for x in b:
        count+=1
        print(x)
        File.write(str(x) + "\n") 
    print(count)
    File.write(str(count) + "\n") 
    File.close()
#输出满足置信度的按照置信度排序的规则
def printconfident(con,arr):
    confident=[]
    for i in arr:
        a=i[0]
        alen=len(a)
        index1=arr.index(i)
        arr1=arr[index1:]
        for j in arr1:
            flag=1 
            b=j[0][:]
            #if a[0]=='茵陈middle(31.02)':
                #print('~')
                #print(b)
            blen=len(b)
            if blen>alen:
                str1=",".join(str(d) for d in a)
                str2=[]
                for x in a:
                    if x not in b:
                        flag=0
                if flag==1:
                    print(a,b)
                    for x2 in a: 
                        b.remove(x2)
                    str2=",".join(str(d) for d in b)
                    str2=str1+'-->>'+str2
                    num=float(j[1])/float(i[1])
                    #求提升度
                    lift=0
                    for z in arr:
                        z1=z[0]
                        if len(b)==len(set(z1)&set(b)):
                            lift=num*12138/z[1]
                    confident.append((str2,float(j[1]),num,lift))
    File = open("hello2.txt", "w")
    y=sorted(confident,key=lambda x:x[1],reverse=True)
    count=0
    for x in y:
        if x[2]>=con:
            #if hasNumbers(str(x[0])):
            count+=1
            print(x)
            File.write(str(x) + "\n") 
            '''
            count+=1
            print(x)
            File.write(str(x) + "\n") 
            '''
        pass
    print(count)
    File.write(str(count) + "\n") 
    File.close() 
'''
#计算不同支持度的输出规则数   
if __name__=="__main__":
    a1,b1=add_matix()
    for i in range(400,600):
        a,b=a1,b1
        beforec=[]
        befored=[]
        cerli=[]
        supli=[]
        count=0
        while True:
            count+=1
            c,d,supli=findtime(b,a,i,supli)
            if len(c)==0:
                break;
            a=makenext(c) 
            #cerli=findcer(beforec,befored,c,d,0.7,cerli)       
            beforec=c
            befored=d
        print(len(supli))
    #printsult(supli,r"home1.txt")
    #print('````````````````')
    #printsult(cerli,r"home2.txt")
    #printconfident(0.9,supli)
'''

#普通输出
if __name__=="__main__":
    a1,b1=add_matix()
    i=400
    a,b=a1,b1
    beforec=[]
    befored=[]
    cerli=[]
    supli=[]
    count=0
    while True:
        count+=1
        c,d,supli=findtime(b,a,i,supli)
        if len(c)==0:
            break;
        a=makenext(c) 
        cerli=findcer(beforec,befored,c,d,0.7,cerli)       
        beforec=c
        befored=d
    printsult(supli,r"home1.txt")
    print('````````````````')
    printsult(cerli,r"home2.txt")
    print('`````2`````````')
    for i in supli:
        print(i)
    print('`````3`````````')
    printconfident(0.7,supli)

