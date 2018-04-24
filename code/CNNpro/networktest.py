import networkx as nx
import matplotlib.pyplot as plt
import xlrd
import numpy as np
#huoqu药物索引
meindex={}
data=xlrd.open_workbook(r'字典索引.xlsx')
table=data.sheets()[0]
rowc=table.nrows
for i in range(rowc):
    meindex[table.row_values(i)[0]]=table.row_values(i)[1]

#将药物对 以其序号的形式存入duilist
medicine={}
data=xlrd.open_workbook(r'计量准备表1.xlsx')
table=data.sheets()[0]
rowc=table.nrows
for i in range(rowc):
    medicine[table.row_values(i)[0]]=[]
for i in range(rowc):
    if table.row_values(i)[1] in meindex.keys():
        medicine[table.row_values(i)[0]].append(meindex[table.row_values(i)[1]])
dui=[]
list=medicine.items()
for key,value in list:
    for i in range(len(value)):
        for j in range(i+1,len(value)):
            dui.append((value[i],value[j]))
dui=set(dui)
#以下部分用于去除（A,B）/（B,A）这种重复
duilist=[]
for i in dui:
    duilist.append([i[0],i[1]])
for i in range(len(duilist)):
    for j in range(i+1,len(duilist)):
        if duilist[i][0]==duilist[j][1] and duilist[i][1]==duilist[j][0]:
            x=duilist[j][0]
            duilist[j][0]=duilist[i][1]
            duilist[i][1]=x
duilist2=[]
for i in duilist:
    duilist2.append((i[0],i[1]))
duilist=set(duilist2)



#形成无向度矩阵
arr=np.zeros((190,190))
for i,j in duilist:
    arr[int(i),int(j)]=1
    arr[int(j), int(i)] = 1
#求每个药的度数
arr1=arr.sum(0)
print(arr1)
'''
arr1[arr1<2]=0
duilist=[]
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[int(i),int(j)]!=0:
            duilist.append((i,j))
print(duilist)
'''
'''
G = nx.Graph()
G.add_edges_from(duilist)  #加边集合
nx.draw(G)
#plt.savefig("youxiangtu.png")
plt.show()
'''