#coding=utf-8
'''
a=np.array([
             [[1.0,3,1],[2,4,9],[11,5,2]],
             [[4,6,11],[5,7,7],[100,90,5]],
             [[8,6,9],[21,17,12],[4,7,9]]            
             ])
'''
'''
a=np.array([
             [[1.0,3,1,9],[2,4,9,15],[11,5,2,4]],
             [[4,6,11,16],[5,7,7,2],[100,90,5,6]],
             [[1,2,9,5],[3,4,12,1],[4,7,9,7]],
             [[2,3,9,5],[5,6,12,1],[4,7,9,8]],
             [[8,6,9,5],[21,17,12,1],[4,7,9,7]]            
             ])
'''
'''
a=np.array([[[1.0,3,1,9],[2,4,9,15],[11,5,2,4]]])
''' 
'''     
a=np.array([
             [[1],[2],[3]],
             [[4],[5],[6]],
             [[7],[8],[9]]           
             ])
'''    
'''             
a=np.array([
             [[1.0,2,3],[4,5,6],[7,8,9]],
             [[1.0,2,3],[4,5,6],[7,8,9]],
             [[1.0,2,3],[4,5,6],[7,8,9]]            
             ])    
'''  
'''
a=np.array(range(196080))
random.shuffle(a)
a=a.reshape(24,190,43)
'''
'''
a=np.array(range(1000))
random.shuffle(a)
a=a.reshape(10,10,10)
'''
'''
a=np.random.rand(24,190,43)
'''   

from itertools import count
import random

from numpy import size, shape

import newdic
import newdic as nd
import numpy as np


def ccarg(a,w,reason,medician):  
    flag0=np.zeros((np.size(a, 0)))
    flag1=np.zeros((np.size(a, 1)))
    flag2=np.zeros((np.size(a, 2)))   
    '''a0=np.array([[[1,2],[3,4]]])'''
    a=a.astype(float)
    def H(a0):
        '''flag0[1]=1
        flag1[1]=1'''        
        aaa=a0-0
        count=0
        count0,count1,count2=np.size(a0,0),np.size(a0,1),np.size(a0,2)
        '''1'''
        for i in flag0:         
            if i==1:
                aaa[count,:,:]=0
                count0=count0-1
            count=count+1
        count=0
        for i in flag1:
            if i==1:
                aaa[:,count,:]=0
                count1=count1-1
            count=count+1
        count=0
        for i in flag2:
            if i==1:
                aaa[:,:,count]=0
                count2=count2-1
            count=count+1  
        a0d=np.sum(aaa, 0)/count0
        a1d=np.sum(aaa, 1)/count1
        a2d=np.sum(aaa, 2)/count2
        avg=np.sum(aaa)/(count0*count1*count2)
        aa=a0-0
        '''print(aaa)
        print(count0,count1,count2,np.sum(aaa[0,:,:]),count1*count2)'''
        b0d=np.array(list(map(lambda i:np.sum(aaa[i,:,:])/(count1*count2),range(np.size(aaa,0)))))            
        for i in range(np.size(aaa,0)):
            aa[i,:,:]=aa[i,:,:]+b0d[i]
        '''print('--1--')
        print(b0d)
        print(aa)'''
        b1d=np.array(list(map(lambda i:np.sum(aaa[:,i,:])/(count0*count2),range(np.size(aaa,1)))))            
        for i in range(np.size(aaa,1)):
            aa[:,i,:]=aa[:,i,:]+b1d[i]
        '''print('--2--')
        print(b1d)
        print(aa)'''
        b2d=np.array(list(map(lambda i:np.sum(aaa[:,:,i])/(count0*count1),range(np.size(aaa,2)))))            
        for i in range(np.size(aaa,2)):
            aa[:,:,i]=aa[:,:,i]+b2d[i]
        '''print('--3--')
        print(b2d)
        print(aa)'''
        '''aa=a0-0'''
        aa=aa-a0d
        '''print('--4--')
        print(a0d)
        print(aa)'''
        b1d=np.zeros((np.size(a0, 1),np.size(a0, 0),np.size(a0, 2)))
        for i in range(size(a0,0)-1,-1,-1):
            for j in range(size(a0,1)):
                for c in range(size(a0,2)):
                    b1d[size(a0,1)-1-j][i][c]=aa[i][j][c]
        b1d=b1d-a1d         
        for i in range(size(b1d,0)-1,-1,-1):
            for j in range(size(b1d,1)):
                for c in range(size(b1d,2)):
                    aa[j][size(b1d,0)-1-i][c]=b1d[i][j][c]
        '''print('--5--')
        print(a1d)
        print(aa) '''           
        a2dd=np.zeros((np.size(a2d,1),np.size(a2d,0)))
        for i in range(size(a2d,0)-1,-1,-1):
            for j in range(size(a2d,1)):
                a2dd[j][size(a2dd,1)-1-i]=a2d[i][j]
        b1d=np.zeros((np.size(a0, 2),np.size(a0, 1),np.size(a0, 0)))           
        for i in range(size(a0,0)-1,-1,-1):
            for j in range(size(a0,2)):
                for c in range(size(a0,1)):
                    b1d[j][c][size(b1d,2)-1-i]=aa[i][c][j]
        b1d=b1d-a2dd          
        for i in range(size(a0,0)-1,-1,-1):
            for j in range(size(a0,2)):
                for c in range(size(a0,1)):
                    aa[size(aa,0)-1-i][c][j]=b1d[j][c][i]
        '''print('--6--')
        print(a2d)
        print(aa)''' 
        aa=aa-avg
        '''print('--7--')
        print(avg)
        print(aa)'''
        aa=aa*aa
        '''print('--8--')
        print(aa)'''
        aa=aa+w*h*2000
        sum=0
        count=0
        for i in range(np.size(aa,0)):       
            if flag0[i]==0:
                for j in range(np.size(aa,1)):
                    if flag1[j]==0:                 
                        for  y in range(np.size(aa,2)):
                            if flag2[y]==0:
                                sum=sum+aa[i,j,y]
                                count=count+1
        if count==0:
            print("无")
            return aa,-1
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
                        for  y in range(np.size(a0,2)):
                            if flag2[y]==0:
                                count=count+1
                                sumV=sumV+a0[i,j,y]
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
                        for  y in range(np.size(a0,2)):
                            if flag2[y]==0:
                                count=count+1
                                sumV=sumV+a0[j,i,y]
                sumV=sumV/count
                if sumV>maxV:
                    maxV=sumV
                    D,I=1,i
        for i in range(np.size(a0,2)):       
            if flag2[i]==0:
                sumV=0
                count=0
                for j in range(np.size(a0,1)):
                    if flag1[j]==0:                
                        for  y in range(np.size(a0,0)):
                            if flag0[y]==0:
                                count=count+1
                                sumV=sumV+a0[y,j,i]
                sumV=sumV/count
                if sumV>maxV:
                    maxV=sumV
                    D,I=2,i
        if D==0:flag0[I]=1
        elif D==1:flag1[I]=1
        elif D==2:flag2[I]=1
        
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
            for i in range(np.size(a0, 2)):
                if flag2[i]==1:
                    flag2[i]=0
                    az,h1=H(a0)
                    if h1>h:
                        flag2[i]=1
                    else:
                        count+=1
                        '''show(a0)'''
                        #print(h1)
                
            if count==0:
                flagvar=0  
                  
    def show(a):
        for i in range(np.size(a,0)): 
            if flag0[i]==0:
                print(i+1)
                print('[')
                for j in range(np.size(a,1)): 
                    if flag1[j]==0:
                        print(reason[j])
                        for y in range(np.size(a,2)): 
                                if flag2[y]==0:
                                    print(medician[y],end=" ")

                        print()
                        for y in range(np.size(a,2)): 
                                if flag2[y]==0:
                                    if sumnum[i,j,y]>1:
                                        print(a[i,j,y],'均',end=" ")
                                        w[i,j,y]=1
                                    else:
                                        print(a[i,j,y],end=" ")
                                        w[i,j,y]=1
                        print()
                print(']')    
        print()        
    h=1
    az,h1=H(a)
    #print(h1)
    while h1>h:
        remove(az)
        az,h1=H(a)
        #print(h1)
        if h1==-1:
            print("11")
    #add(a,h)
    print('------------------------------------------------------------------------------')

    show(a)
    return w

countall=10
reason,medician=newdic.add_showdic()
a,sumnum,w=nd.add_matix() 
for t in range(countall):
    w=ccarg(a, w,reason,medician)
    