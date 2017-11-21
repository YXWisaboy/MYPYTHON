from scipy import io as spio
import numpy as np
from sklearn import svm
from sklearn.linear_model import LogisticRegression
import os
import csv
import time
t1=time.time()
def get_data(filename):
    lines = csv.reader(open(filename, "r"))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]
    dataset=np.array(dataset)
    return dataset[:,0:np.size(dataset,1)-1],dataset[:,-1]
X,Y = get_data(r'逻辑回归训练集.csv')
model = LogisticRegression()
model.fit(X, Y) # 拟合
predict = model.predict(X) #预测     逻辑回归测试集.csv 
t2=time.time() 

print(u"预测准确度为：%f%%"%(np.mean(np.float64(predict == Y))*100))
print((t2-t1)*1000,'ms')