import xlrd
import xlwt

import numpy as np

data=xlrd.open_workbook(r'C:\Users\sjzx\Desktop\柴胡单位换算准备表.xlsx')
table=data.sheets()[0]
rowc=table.nrows
col=table.ncols
a=''
b=''
f = xlwt.Workbook()
sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
li1=[]
li2=[]
arr=[]
a=-1
x=0
for i in range(rowc):
    print(i)
    if table.row_values(i)[0]==a:
        li2.append(table.row_values(i)[2])
        a=table.row_values(i)[0]
    elif table.row_values(i)[0]!=a:
        li1=li1+li2
        for t in range(len(li1)):
            sheet1.write(x,t,li1[t])
        li1=[]
        li2=[]
        li2.append(table.row_values(i)[2])
        li1.append(table.row_values(i)[0])
        li1.append(table.row_values(i)[1])
        a=table.row_values(i)[0]
        x+=1      
f.save(r'C:\Users\sjzx\Desktop\test.xls') #保存文件         
print(1)