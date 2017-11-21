import numpy as np
import csv

def get_data(filename):
    lines = csv.reader(open(filename, "r"))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]
    dataset=np.array(dataset)
    return dataset[:,0:np.size(dataset,1)-1],dataset[:,-1]
X,Y = get_data(r'逻辑回归训练集.csv')


#print(w,b)
def logis(X,Y,w,b,m):
    a=1.0/(1+np.exp(-(np.dot(X,w)+b)))
    f=a-Y
    db=np.sum(f)/len(f)
    dw=np.dot(X.T,f)/len(f)
    w=w-m*dw
    b=b-m*db
    return w,b

m=0.0001
w=np.random.rand(np.size(X,1))
b=np.random.rand()

for i in range(12000):
    w,b=logis(X,Y,w,b,m)
    a=1.0/(1+np.exp(-(np.dot(X,w)+b)))
    a=np.where(a<=0.5,0,1)

    print(np.mean(np.float64(a == Y))*100)

