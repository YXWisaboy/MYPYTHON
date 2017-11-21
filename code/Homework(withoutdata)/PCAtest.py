from sklearn.decomposition import PCA 
import csv
import numpy as np
from sklearn.linear_model import LogisticRegression
import keras.utils
from keras.models import Sequential
from keras.layers import Dense, Activation

#n_components:  
#意义：PCA算法中所要保留的主成分个数n，也即保留下来的特征个数n
#类型：int 或者 string，缺省时默认为None，所有成分被保留。
#赋值为int，比如n_components=1，将把原始数据降到一个维度。
#赋值为string，比如n_components='mle'，将自动选取特征个数n，使得满足所要求的方差百分比。

def get_data(filename):
    lines = csv.reader(open(filename, "r"))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]
    dataset=np.array(dataset)
    return dataset[:,0:np.size(dataset,1)-1],dataset[:,-1]
X,Y = get_data(r'逻辑回归训练集.csv')
pca=PCA(n_components=0.99)
newData=pca.fit_transform(X)
print(pca.explained_variance_ratio_)
print(newData)

'''
model = LogisticRegression()
model.fit(newData, Y) # 拟合
predict = model.predict(newData) #预测     逻辑回归测试集.csv 
print(u"预测准确度为：%f%%"%(np.mean(np.float64(predict == Y))*100))
'''

y_train = keras.utils.to_categorical(Y, num_classes=2)
model = Sequential()
model.add(Dense(32, input_shape=(5,)))
model.add(Activation('relu'))
model.add(Dense(32))
model.add(Activation('relu'))
model.add(Dense(2))
model.add(Activation('softmax'))
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
model.fit(newData, y_train,epochs=50,batch_size=32)
score = model.evaluate(newData, y_train, batch_size=128)
print(score)
