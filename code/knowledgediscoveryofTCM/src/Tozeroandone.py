import numpy as np
import xlrd
import xlwt
import re
from numpy import int, int0
from builtins import int
import math
def add_dic(table,dic):
    rowc=table.nrows
    col=table.ncols
    for i in range(rowc):
        dic[table.row_values(i)[0]]=table.row_values(i)[1]
        #print(table.row_values(i)[0],table.row_values(i)[1])
    return dic

medicine={}
data=xlrd.open_workbook(r'柴胡分析.xlsx')
table=data.sheets()[4]
medicine=add_dic(table, medicine)
arr1=np.zeros((1066,25))
table=data.sheets()[0]
rowc=table.nrows
for i in range(rowc):
    flag2=medicine.get(table.row_values(i)[2],-1)
    if flag2!=-1 and str(table.row_values(i)[3]).strip()!='':
        x=int(table.row_values(i)[0])-1
        y=int(medicine[table.row_values(i)[2]])
        #print(table.row_values(i)[0],str(table.row_values(i)[3]).strip())
        arr1[x,y] =1
f = xlwt.Workbook()
sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
count=0
for i in medicine:
    sheet1.write(0,count,i)
    count+=1
for x in range(np.size(arr1, 0)):
    for y in range(np.size(arr1, 1)):
        sheet1.write(x+1,y,arr1[x,y])
      
f.save(r'C:\Users\sjzx\Desktop\test.xls')