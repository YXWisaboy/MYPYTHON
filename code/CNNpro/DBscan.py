import numpy as np
import xlrd
from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
data=xlrd.open_workbook(r'数据准备表3（聚类）.xlsx')
table=data.sheets()[0]
rowc=table.nrows
cols=table.ncols
arr=[]
for i in range(rowc):
    x=table.row_values(i)
    arr.append(x)
arr=np.array(arr)
#data = StandardScaler().fit_transform(arr)
print(arr[180])
model = KMeans(n_clusters=7, init='k-means++', n_init=5)
y_pred = list(model.fit_predict(arr))
print(y_pred)
#model = DBSCAN(eps=50, min_samples=6)
#model.fit(arr)
#y= model.labels_
#print(y)
dic={}
for i in range(len(y_pred)):
    dic.setdefault(y_pred[i],[])
    dic[y_pred[i]].append(i)
for i in dic.items():
    print(i)