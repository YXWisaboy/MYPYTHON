import numpy as np
import xlrd
import pandas as pd
#将病机转化为1 2 3的形式
data=xlrd.open_workbook(r'数据准备表2.xlsx')
table=data.sheets()[3]
rowc=table.nrows
y=[]
list1=['气阴两伤','气阴两虚','阴伤气耗','肾虚气阴两伤','气阴交亏']
list2=['痰瘀郁肺','痰瘀阻肺','痰瘀互结','痰瘀阻络','风痰瘀阻','痰浊瘀阻']
for i in range(rowc):
    x1=table.row_values(i)[0]
    x2=table.row_values(i)[1]
    a=0
    b=0
    ab=0
    if x1 in list1 or x2 in list1:
        a = 1
    if x1 in list2 or x2 in list2:
        b = 2
    ab=a+b
    y.append(ab)
print(y)
y=np.array(y).reshape(-1,1)
csv_pd = pd.DataFrame(y)
csv_pd.to_csv(r'C:\Users\sjzx\Desktop\test.csv', sep=',', header=False, index=False)
