#该算法生成肺癌数据的关联分析准备表，接下来就可以据此进行关联分析了
import xlrd
import xlwt
import pandas as pd
#将原始数据表转化成ID为行，200余种药物为列的形式
medicine={}
data=xlrd.open_workbook(r'数据准备表2.xlsx')
table=data.sheets()[5]
rowc=table.nrows
cols=table.ncols
arr=[]
f = xlwt.Workbook()
sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
for i in range(rowc):
        k=0
        for j in range(cols-1):
                if table.row_values(i)[j]!=0:
                        sheet1.write(i, k, j)
                        k+=1
f.save(r'C:\Users\sjzx\Desktop\test.xls')