from scipy import misc
import matplotlib.pyplot as plt
from numpy import *
l = misc.imread('T1cQP8FbpfXXXXXXXX_!!0-item_pic.jpg')
x=l.shape[0]
y=l.shape[1]
def exl(size):
    arr=arange(size)
    '这里另所有能被4整除的对角线位置设为黑色'
    return arr%4==0
l1=l.copy()
x1=exl(x)
y1=exl(y)
l1[x1,y1]=0
'图形位置函数subplot中（a,b,c）为纵向a列，横向b列的格子中，处于第c个格子'
plt.subplot(121)
plt.imshow(l1)
l2=l.copy()
'在这里运用布尔变量索引，返回的其实为BOOL为真值的位置'
l2[(l>l.max()/4)&(l<l.max()*3/4)]=0
plt.subplot(122)
plt.imshow(l2)
plt.show()
