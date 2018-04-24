import FCM
import numpy as np
import xlrd
import pandas as pd 
def makeGroup():
    data=xlrd.open_workbook(r'分组准备表1.xlsx')
    table=data.sheets()[0]
    rowc=table.nrows
    dicid={}
    dicnum={}
    dicpingid={}
    for i in range(rowc):
        dicid[table.row_values(i)[1]]=[]
        dicnum[table.row_values(i)[1]]=[]
        dicpingid[table.row_values(i)[1]]=[]
    for i in range(rowc):
        dicid[table.row_values(i)[1]].append(table.row_values(i)[0])
        dicnum[table.row_values(i)[1]].append(table.row_values(i)[2])
        dicpingid[table.row_values(i)[1]].append(table.row_values(i)[3])
    for i in dicid:
        dicid[i]=np.array(dicid[i])
        dicnum[i]=np.array(dicnum[i])
        dicpingid[i]=np.array(dicpingid[i])
    return dicid,dicnum,dicpingid
def sortbydic(a,c):
    max1=c.index(max(c))
    min1=c.index(min(c))
    mid=3-max1-min1
    arr=np.array(a)
    #print(arr)
    arr1=arr-0
    arr1[:,0]=arr[:,min1]
    arr1[:,1]=arr[:,mid]
    arr1[:,2]=arr[:,max1]
    #print(arr1)
    c1=[]
    c1.append(c[min1])
    c1.append(c[mid])
    c1.append(c[max1])
    return arr1,c1
dicid,dicnum,dicpingid=makeGroup()
arr=[]
cdic={}
for i in dicid:
    if len(set(dicnum[i]))>4:
        #print(i)
        arr1,c=FCM.fcm(dicnum[i])
        #使数据按照大中小剂量排列
        #print(arr1)
        arr2,d=sortbydic(arr1, c)        
        for j in range(len(arr2)):
            li=[]
            li.append(i)
            li.append(dicid[i][j])
            li.append(dicpingid[i][j])
            li.append(dicnum[i][j])
            li.append(list(arr2[j]))
            arr.append(li)
        cdic[i]=d
for i in cdic:
    print(i,cdic[i])
csv_pd = pd.DataFrame(arr)  
csv_pd.to_csv(r'C:\Users\sjzx\Desktop\test.csv', sep=',', header=False, index=False) 