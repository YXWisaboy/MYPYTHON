import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import xlrd
#取数据
data=xlrd.open_workbook(r'数据准备表2.xlsx')
table=data.sheets()[5]
rowc=table.nrows
cols=table.ncols
arr=[]
for i in range(rowc):
    x=table.row_values(i)
    arr.append(x)
arr=np.array(arr)
x=arr[:,0:cols-1]
y=arr[:,cols-1:cols]
print(x.shape,y.shape)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
print(x_train.shape,y_train.shape)
model = RandomForestClassifier(n_estimators=100, criterion='gini', max_depth=10, oob_score=True)
model.fit(x_train, y_train.ravel())

y_train_pred = model.predict(x_train)
acc_train = accuracy_score(y_train, y_train_pred)
y_test_pred = model.predict(x_test)
acc_test = accuracy_score(y_test, y_test_pred)
print('\t训练集准确率: %.4f%%' % (100*acc_train))
print('\t测试集准确率: %.4f%%\n' % (100*acc_test))
c=[round(z,2) for z in model.feature_importances_*10000]
#print(len(model.feature_importances_),model.feature_importances_*10000)
c=np.array(c).reshape(-1,1)
csv_pd = pd.DataFrame(c)
csv_pd.to_csv(r'C:\Users\sjzx\Desktop\test.csv', sep=',', header=False, index=False)

