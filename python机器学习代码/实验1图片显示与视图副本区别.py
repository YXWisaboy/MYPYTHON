from scipy import misc
import matplotlib.pyplot as plt

l = misc.imread('T1cQP8FbpfXXXXXXXX_!!0-item_pic.jpg')
x=l.shape[0]
y=l.shape[1]
x1=x
y1=y
l[range(x),range(y)]=0
l[range(x-1,-1,-1),range(y)]=0
    

plt.imshow(l)
plt.show()
