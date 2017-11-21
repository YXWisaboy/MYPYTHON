import numpy as np
import xlrd
def add_matix():
    data=xlrd.open_workbook(r'预处理测试.xlsx')
    table=data.sheets()[0]
    arr=[]
    list=[]
    rowc=table.nrows
    for i in range(rowc):
        for j in table.row_values(i):
            if j!='':
                list.append(j)
        arr.append(list)
        list=[]
    return arr
def group_matix(a):
    b=[]
    for i in a:
        if len(b)==0:
            b.append(i[1:])
        else:
            flat=0
            for j in b:
                if j[0:2]==i[1:3]:                
                    j[2]+=i[3]
                    flat=1
            if flat==0:
                b.append(i[1:])
    return b
def lift_matix(b,sup):
    c=[]
    s=[]
    
    for i in b:
        flat=0    
        for j in s:
            if i[0]==j[0]:
                if i[2]>j[2]:
                    j[1:]=i[1:]
                flat=1
        if flat==0:
            s.append(i)
    for i in s:
        if i[2]>=sup:
            c.append(i)
    return c
a=add_matix()
print(a)
b=group_matix(a)
print(b) 
c=lift_matix(b,1)      
print(c)
        
    