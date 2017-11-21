import numpy as np
import time
import string
a=np.random.rand(100000)#生成随机数矩阵，用法同哦呢，zero
b=np.random.rand(100000)
'''获取当前时间'''
t1=time.time()
c=np.dot(a,b)
t2=time.time()
print('Using time1 is '+str(1000*(t2-t1))+'ms')
t1=time.time()
for i in range(100000):
    c+=a[i]*b[i]
t2=time.time()
print('Using time2 is '+str(1000*(t2-t1))+'ms')
