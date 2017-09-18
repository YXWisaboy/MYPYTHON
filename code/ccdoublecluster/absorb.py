#coding=utf-8
import numpy as np
import xlrd
import xlwt
import re
m=re.compile(r'(\D*)(\d*)')
n=re.compile(r'\d{4}(\d{2})\S*')
data=xlrd.open_workbook(r'C:\Users\sjzx\Desktop\去空后的可用表.xlsx')
table=data.sheets()[0]
rowc=table.nrows
col=table.ncols
li=[]
arr=np.array(['ID','time','reason1','reason2','madicien','num'])
for i in range(rowc):
    print(i)
    if i==0:
        continue
    na=n.match(table.row_values(i)[1])
    for j in range(6,col):
        
        li=[]
        li.append(table.row_values(i)[0])
        li.append(na.group(1))        
        li.append(table.row_values(i)[2])
        li.append(table.row_values(i)[3])
        value=table.row_values(i)[j]
        if value!='':
            ma=m.match(value)
            li.append(ma.group(1))
            if ma.group(2)!='':
                li.append(float(ma.group(2)))
                arr=np.vstack((arr,np.array(li)))
            else:
                li.append(0)
                arr=np.vstack((arr,np.array(li)))
#print(arr)
f = xlwt.Workbook()
sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
for i in range(np.size(arr, 0)):
    for j in range(np.size(arr, 1)):
        sheet1.write(i,j,arr[i,j])
f.save(r'C:\Users\sjzx\Desktop\test.xls') #保存文件         
print(1)

