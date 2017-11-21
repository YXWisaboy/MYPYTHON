#coding=utf-8
import numpy as np
from itertools import count
from numpy import size, shape
import random
import newdic2 as nd
import newdic2
import math

def ccarg(a,w,reason,medician): 
    flag0=np.zeros((np.size(a, 0)))
    flag1=np.zeros((np.size(a, 1)))
    def H(a0):
        '''flag0[1]=1
        flag1[1]=1'''        
        aaa=a0-0
        count=0
        count0,count1=np.size(a0,0),np.size(a0,1)
        '''1'''
        for i in flag0:         
            if i==1:
                aaa[count,:]=0
                count0=count0-1
            count=count+1
        count=0
        for i in flag1:
            if i==1:
                aaa[:,count]=0
                count1=count1-1
            count=count+1
        a0d=np.sum(aaa, 0)/count0
        a1d=np.sum(aaa, 1)/count1
        avg=np.sum(aaa)/(count0*count1)
        '''print(a0)'''
        aa=a0-0
        aa=aa-a0d
        '''print('=============1=====================')
        print(a0d)
        print(aa)'''
        b1d=np.zeros((np.size(a0, 1),np.size(a0, 0)))
        for i in range(size(a0,0)-1,-1,-1):
            for j in range(size(a0,1)):
                b1d[size(a0,1)-1-j][i]=aa[i][j]
        b1d=b1d-a1d         
        for i in range(size(b1d,0)-1,-1,-1):
            for j in range(size(b1d,1)):
                aa[j][size(b1d,0)-1-i]=b1d[i][j]
        '''print('=============2=====================')
        print(a1d)
        print(aa)'''
        
        aa=aa+avg
        '''print('=============2=====================')
        print(avg)
        print(aa)'''
        aa=aa*aa
        aa=aa+w*h*2000
        sum=0
        count=0
        for i in range(np.size(aa,0)):       
            if flag0[i]==0:
                for j in range(np.size(aa,1)):
                    if flag1[j]==0:
                        sum=sum+aa[i,j]
                        count=count+1
        if count==0:
            print("无")
            return aa,-1
        '''print('=============sum=====================')
        print(aa)
        print(count)'''
        return aa,sum/count
    def remove(a0):
        sumV=0
        maxV=0
        D=-1
        I=-1
        for i in range(np.size(a0,0)):       
            if flag0[i]==0:
                sumV=0
                count=0
                for j in range(np.size(a0,1)):
                    if flag1[j]==0:                
                        count=count+1
                        sumV=sumV+a0[i,j]
                sumV=sumV/count
                if sumV>maxV:
                    maxV=sumV
                    D,I=0,i
        for i in range(np.size(a0,1)):       
            if flag1[i]==0:
                sumV=0
                count=0
                for j in range(np.size(a0,0)):
                    if flag0[j]==0:                                   
                        count=count+1
                        sumV=sumV+a0[j,i]
                sumV=sumV/count
                if sumV>maxV:
                    maxV=sumV
                    D,I=1,i
        if D==0:flag0[I]=1
        elif D==1:flag1[I]=1
    def add(a0,h):
        flagvar=1
        while flagvar==1:
            count=0
            for i in range(np.size(a0, 0)):
                if flag0[i]==1:
                    flag0[i]=0
                    az,h1=H(a0)
                    if h1>h:
                        flag0[i]=1
                    else:
                        count+=1
                        '''show(a0)'''
                        #print(h1)
            for i in range(np.size(a0, 1)):
                if flag1[i]==1:
                    flag1[i]=0
                    az,h1=H(a0)
                    if h1>h:
                        flag1[i]=1
                    else:
                        count=count+1
                        '''show(a0)'''
                        #print(h1)
            if count==0:
                flagvar=0 
    def show(a):
        for j in range(np.size(a,1)): 
            print('          ',end=" ") 
            if flag1[j]==0:
                print(medician[j],end=" ") 
        print()
        for i in range(np.size(a,0)): 
            if flag0[i]==0:
                print(reason[i],end=" ")
                for j in range(np.size(a,1)): 
                    if flag1[j]==0:                            
                        print(math.exp(a[i,j]),end=" ")
                        w[i,j]=1
                print()  
        print()         
    h=0.05
    az,h1=H(a)
    #print(h1)
    while h1>h:
        remove(az)
        az,h1=H(a)
        #print(h1)
        if h1==-1:
            print("11")
    add(a,h)
    print('------------------------------------------------------------------------------')
    
    show(a)
    return w 

countall=20
reason,medician=newdic2.add_showdic()
a,w=nd.add_matix() 

for t in range(countall):
    w=ccarg(a, w,reason,medician)   

#a=np.array([[0,2,6],[3,4,11],[9,15,10]])   
#w=ccarg(a, w,reason,medician) 