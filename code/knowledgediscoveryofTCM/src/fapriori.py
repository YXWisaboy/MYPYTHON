from multiprocessing.dummy import list
import xlrd
def add_matix():
    data=xlrd.open_workbook(r'模糊关联实验数据.xlsx')
    table=data.sheets()[2]
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
            name.append(table.row_values(i)[1]+'low')
            name.append(table.row_values(i)[1]+'middle')
            name.append(table.row_values(i)[1]+'high')
            if table.row_values(i)[3]!=0:
                drgnum[table.row_values(i)[1]+'low']=table.row_values(i)[3]
            if table.row_values(i)[4]!=0:
                drgnum[table.row_values(i)[1]+'middle']=table.row_values(i)[4]
            if table.row_values(i)[5]!=0:
                drgnum[table.row_values(i)[1]+'high']=table.row_values(i)[5]
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
    
a,b=add_matix()
print(1)
beforec=[]
befored=[]
cerli=[]
supli=[]
count=0
while True:
    count+=1
    print(count)
    c,d,supli=findtime(b,a,500,supli)
    if len(c)==0:
        break;
    a=makenext(c) 
    cerli=findcer(beforec,befored,c,d,0.7,cerli)       
    beforec=c
    befored=d

printsult(supli,r"home1.txt")
print('````````````````')
printsult(cerli,r"home2.txt")

