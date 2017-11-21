#coding=utf-8
import re

import xlrd
import xlwt

import numpy as np


n=re.compile(r'(\D*)(\d*\.?\d*)(\S*)')
data=xlrd.open_workbook(r'C:\Users\sjzx\Desktop\柴胡整理后期3.xlsx')
table=data.sheets()[0]
rowc=table.nrows
col=table.ncols
li=[]
arr=np.array(['ID','time','book','name','other1','other2','medician','num','unit'])
for i in range(rowc):
    print(i)
    for j in range(6,col):        
        li=[]
        li.append(table.row_values(i)[0])
        li.append(table.row_values(i)[1])    
        li.append(table.row_values(i)[2])
        li.append(table.row_values(i)[3])
        li.append(table.row_values(i)[4])    
        li.append(table.row_values(i)[5])
        value=str(table.row_values(i)[j])
        if value!='':
            ma=n.match(value)
            li.append(ma.group(1))
            if ma.group(2)!='':
                li.append(float(ma.group(2)))
            else:
                li.append(' ')
#print(arr)
            if ma.group(3)!='':
                li.append(ma.group(3))
            else:
                li.append(' ')
            arr=np.vstack((arr,np.array(li)))
f = xlwt.Workbook()
sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
for i in range(np.size(arr, 0)):
    for j in range(np.size(arr, 1)):
        sheet1.write(i,j,arr[i,j])
f.save(r'C:\Users\sjzx\Desktop\test.xls') #保存文件         
print(1)
