import FCM
import numpy as np
import xlrd
import pandas as pd 
def makeGroup():
    data=xlrd.open_workbook(r'分组准备表.xlsx')
    table=data.sheets()[0]
    rowc=table.nrows
    dicid={}
    dicnum={}
    for i in range(rowc):
        dicid[table.row_values(i)[1]]=[]
        dicnum[table.row_values(i)[1]]=[]
    for i in range(rowc):
        dicid[table.row_values(i)[1]].append(table.row_values(i)[0])
        dicnum[table.row_values(i)[1]].append(table.row_values(i)[2])
    for i in dicid:
        dicid[i]=np.array(dicid[i])
        dicnum[i]=np.array(dicnum[i])
        
    return dicid,dicnum
dicid,dicnum=makeGroup()
arr=[]
for i in dicid:
    if len(set(dicnum[i]))>4:
        
        arr1=FCM.fcm(dicnum[i])
        for j in range(len(arr1)):
            li=[]
            li.append(i)
            li.append(dicid[i][j])
            li.append(dicnum[i][j])
            li.append(arr1[j])
            arr.append(li)
    
csv_pd = pd.DataFrame(arr)  
csv_pd.to_csv(r'C:\Users\sjzx\Desktop\test.csv', sep=',', header=False, index=False) 