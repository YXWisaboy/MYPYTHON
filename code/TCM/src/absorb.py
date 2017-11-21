import xlrd
import xlwt
import numpy as np

data=xlrd.open_workbook(r'C:\Users\sjzx\Desktop\方剂数据预处理（共享杯）\主治表.xlsx')
table=data.sheets()[0]
rowc=table.nrows
col=table.ncols
li=[]
for i in range(rowc):
    print(i)
    for j in range(col):
        if table.row_values(i)[j]!='':
            li.append(table.row_values(i)[j])
f = xlwt.Workbook()
sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
for i in range(len(li)):
    sheet1.write(i,0,li[i])
f.save(r'C:\Users\sjzx\Desktop\方剂数据预处理（共享杯）\test.xlsx') #保存文件         
print('success')
        
    