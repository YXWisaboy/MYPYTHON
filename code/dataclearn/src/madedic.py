#coding=utf-8
import numpy as np
import xlrd
import xlwt
import re
data=xlrd.open_workbook(r'C:\Users\sjzx\Desktop\字典索引.xlsx')
dic1={}
dic2={}
table=data.sheets()[0]
rowc=table.nrows
col=table.ncols
for i in range(rowc):
    dic1[table.row_values(i)[0]]=table.row_values(i)[1]
table=data.sheets()[1]
rowc=table.nrows
col=table.ncols
for i in range(rowc):
    dic2[table.row_values(i)[0]]=table.row_values(i)[1]
print(dic1)
print(dic2)