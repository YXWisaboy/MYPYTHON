import numpy as np
import random
import xlrd
import xlwt
from numpy import int16
import pandas as pd 
import matplotlib.pyplot as plt

def add_matix():
    data=xlrd.open_workbook(r'模糊关联实验数据.xlsx')
    table=data.sheets()[1]
    rowc=table.nrows
    arr=np.zeros(rowc)
    for i in range(rowc):
        #print(i)
        arr[i]=table.row_values(i)[1]
    return arr
def makeFU(points,c):
    n=len(points)
    c=int(c)
    a=np.zeros((n,c))
    for i in range(n):
        b=np.zeros((c))
        sum=0
        for j in range(c):
            b[j]=random.random();
            sum+=b[j]
        for j in range(c):
            b[j]=b[j]/sum
        a[i]=b
    return a

def alg_fcm(points,u,m,p,e, terminateturn=1000):  
    assert(len(points) == len(u));  
    assert(len(points) > 0);  
    assert(len(u[0]) > 0);  
    assert(m > 0);  
    assert(p > 0);  
    assert(e > 0);  
  
    u1 = u;  
    k = 0;  
    while(True):  
        # calculate one more turn  返回新的矩阵
        u2 = fcm_oneturn(points, u1, m, p);  
        # max difference between u1 and u2  比较新旧两矩阵不同
        maxu = fcm_maxu(u1,u2);  
        print(k)  
        if (maxu < e):  
            break;  
        u1 = u2;  
        k=k+1;  
        if k > terminateturn:  
            break;  
          
    return (u2, k); 
 
def fcm_oneturn(points, u, m, p):  
    assert(len(points) == len(u));  
    assert(len(points) > 0);  
    assert(len(u[0]) > 0);  
    assert(m > 0);  
    assert(p > 0);  
  
    n = len(points);  
    c = len(u[0]);  
  
    # calculate centroids of clusters 计算中心点
    centroids = fcm_c(points, u, m);  
    assert(len(centroids) == c);  
      
    # calculate new u matrix  计算新的划分矩阵
    u2 = fcm_u(points, centroids, m, p);  
    assert(len(u2) == n);  
    assert(len(u2[0]) == c);  
      
    return u2;  

def fcm_maxu(u1,u2):  
    assert(len(u1) == len(u2));  
    assert(len(u1) > 0);  
    assert(len(u1[0]) > 0);  
  
    ret = 0;  
    n = len(u1);  
    c = len(u1[0]);  
    for i in range(n):  
        for j in range(c):  
            ret = max(np.fabs(u1[i][j] - u2[i][j]), ret);  
      
    return ret;  

def fcm_u(points, centroids, m, p):  
    assert(len(points) > 0);  
    assert(len(centroids) > 0);  
    assert(m > 1);  
    assert(p > 0);  
  
    n = len(points);  
    c = len(centroids);  
    ret = [[0 for j in range(c)] for i in range(n)];  
    for i in range(n):  
        for j in range(c):  
            sum1 = 0;  
            d1 = dis_minkowski(points[i],centroids[j],p);  
            for k in range(c):  
                d2 = dis_minkowski(points[i],centroids[k],p);  
                if d2!= 0:  
                    sum1 += np.power(d1/d2, float(2)/(float(m)-1));  
            if sum1!=0:  
                ret[i][j] = 1/sum1;  
  
    return ret;   

def dis_minkowski(rating1, rating2, r):
    distance = 0
    if(isinstance(rating1,list)==True):
        assert(len(rating1) ==len(rating2));  
        for key in range(len(rating1)):
            distance += pow(abs(rating1[key] - rating2[key]),r)
    else:
        distance += pow(abs(rating1 - rating2),r)
    return pow(distance, 1.0/r)#Indicates no ratings in common
    
def fcm_c(points, u, m):  
    assert(len(points) == len(u));  
    assert(len(points) > 0);  
    assert(len(u[0]) > 0);  
    assert(m > 0);  
    
    n = len(points);  
    c = len(u[0]);  
    ret = [];  
    for j in range(c):  
        sum1 = 0;  
        sum2 = 0;  
        for i in range(n):  
            sum2 += np.power(u[i][j], m);  
            sum1 += np.dot(points[i], np.power(u[i][j], m));  
        if sum2!= 0:  
            cj = sum1 /sum2;  
        else:  
            cj = [0 for d in range(len(points[i]))];  
        ret.append(cj);  
    
    return ret; 
def movepromote(points,a):
    a=a.tolist()
    dic={}
    dicpoint={}
    c=len(a[0])
    x=len(a)
    for i in range(x):
        dic.setdefault(points[i],a[i])
    dic = sorted(dic.items(), key=lambda x: float(x[0]), reverse=False)
    
    
    for i in range(c):
        li=[]
        for k in range(len(dic)):
            li.append(dic[k][1][i])
        _positon = li.index(max(li)) 
        for j1 in range(_positon,0,-1):
            if li[j1-1]>li[j1]:
                li[j1-1]=0
        for j1 in range(_positon,len(dic)-1):
            if li[j1+1]>li[j1]:
                li[j1+1]=0
        for k in range(len(dic)):
            dic[k][1][i]=li[k]
    
    for i in range(len(dic)):
        dicpoint[dic[i][0]]=dic[i][1]
    arr=[]
    for i in range(x):
          arr.append(dicpoint[points[i]])
    return dic,arr

def fcm(points):
    u=makeFU(points,3)
    print(points,u)
    #参数分别是初始数据集，初始中心点，参数1，参数2，误差，最高迭代次数
    (result,k)=alg_fcm(points,u,2,2,0.01, 100)
    result=np.reshape(result, (len(result),3))    
    result,arr=movepromote(points,result)
    return arr


#csv_pd = pd.DataFrame(arr)  
#csv_pd.to_csv(r'C:\Users\sjzx\Desktop\test.csv', sep=',', header=False, index=False)      
#print(1)
