import numpy as np
import xlrd
import xlwt
import pandas as pd
#将原始数据表转化成ID为行，200余种药物为列的形式
medicine={}
data=xlrd.open_workbook(r'字典索引.xlsx')
table=data.sheets()[0]
rowc=table.nrows
for i in range(rowc):
        medicine[table.row_values(i)[0]]=table.row_values(i)[1]
data=xlrd.open_workbook(r'计量准备表1.xlsx')
table=data.sheets()[0]
rowc=table.nrows
arr=np.zeros((1090,190))
for i in range(rowc):
    x=int(table.row_values(i)[0])
    y=int(medicine.get(table.row_values(i)[1],-1))
    if y!=-1:
        arr[x,y]=table.row_values(i)[2]
print(arr)
f = xlwt.Workbook()
sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
