from sklearn.decomposition import PCA 
import numpy as np
import os
from PIL import Image
from pylab import *
from scipy import misc
import pylab
def load_data():   

    imgs = os.listdir("./mnisttest")
    num = len(imgs)
    data = np.empty((num,784),dtype="float32")
    label = np.empty((num,),dtype="uint8")
    for i in range(num):
        #print(i,end=' ')
        img = Image.open("./mnisttest/"+imgs[i])
        arr = np.asarray(img,dtype="float32")
        arr=arr.reshape(1,784)
        data[i,:] = arr
        label[i] = int(imgs[i].split('.')[0])
        print(label[i])
        #data /= np.max(data)
        #data -= np.mean(data)
    return data,label
X,Y = load_data()

#pca=PCA(n_components=0.99)
pca=PCA()
newData=pca.fit_transform(X)
print(pca.explained_variance_ratio_)
print(pca.n_components_)
print(newData)

for i in range(10):
    arr1=(X[i,:]).reshape(28,28)
    arr=(newData[i,:]).reshape(28,28)
    arr3=np.zeros((28,10))
    #arr=np.hstack((arr1,arr3,arr2))
    misc.imsave(r'.\testimage\testimage'+str(i)+'.jpg', arr)
show()