from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
l = misc.imread('T1cQP8FbpfXXXXXXXX_!!0-item_pic.jpg')
x=l.shape[0]
y=l.shape[1]
def exl(size):
    arr=np.arange(size)
    '随机打乱数组函数，shuffle含义为洗牌'
    np.random.shuffle(arr)
    return arr
x1=exl(x)
y1=exl(y)
'这里的xi函数生成以x1为行坐标，y1为列坐标的一个索引矩阵，即生成位置列表'
plt.imshow(l[np.ix_(x1,y1)])
plt.show()
