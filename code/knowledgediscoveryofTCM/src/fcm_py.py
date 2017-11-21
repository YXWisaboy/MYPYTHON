#! /usr/bin/env python
#coding=utf-8
import random
import re
import math
from time import clock as now
import numpy as np
import matplotlib.pyplot as plt

def drange(start,stop,step):
    r=start
    res=[]
    while r<stop:
        res.append(r)
        r+=step
    return res
def GetListMaxIndex(l):#获取列表最大值及索引位置
    index=None
    max_value=None
    for i in range(len(l)):
        if not max_value:
            index=i
            max_value=l[i]
        elif max_value<l[i]:
            max_value=l[i]
            index=i
    return index,max_value
def ListAdd(l1,l2):
    if len(l1)!=len(l2):
        raise 'ERROR:length error'
    for i in range(len(l1)):
        l1[i]+=l2[i]
    return l1
def ListSub(l1,l2):
    if len(l1)!=len(l2):
        raise 'ERROR:length error'
    for i in range(len(l1)):
        l1[i]-=l2[i]
    return l1

def ListMulObj(l1,obj):
    if type(obj)==list:
        for i in range(len(l1)):
            l1[i]*=obj[i]
    else:
        for i in range(len(l1)):
            l1[i]*=obj
    return l1
class PATTERN:
    '''
    a=[]#a存放样本各维值
    b=[]#b存放样本对于各类的隶属度
    mesion=0#样本维数
    cata=0#类数
    x=0#x用于最终输出样本所属类
    r='e'#数据真实类别
    '''
    def __init__(self,n1=0,n2=0,r=None):
        self.mesion=n1
        self.cata=n2
        self.a=[]
        self.b=[]
        self.x=0
        self.r=r
        self.cq=[]
        self.e=True
        self.id=None
        for i in range(n1):
            self.a.append(None)
        for i in range(n2):
            self.b.append(None)
    def Set(self,n1=0,n2=0,r=None):
        self.mesion=n1
        self.cata=n2
        self.a=[]
        self.b=[]
        self.r=r
        for i in range(n1):
            self.a.append(None)
        for i in range(n2):
            self.b.append(None)
        self.x=0
class FCM:
    '''
    adi_pattern=[]#样本数组
    centerfcm=[]#聚类中心
    n_numpattern=0#样本个数
    n_dimension=0#样本维数
    n_catacount=0#分类个数
    f_weightm=0#指数m
    min_dis=0#样本与各类中心值得距离的界限
    '''
    def __init__(self,n1=0,n2=0,n3=0,m=0,x=0):
        self.n_numpattern=n1
        self.n_dimension=n2
        self.n_catacount=n3
        self.f_weightm=m
        self.min_dis=x
        self.adi_pattern=[]
        self.datas=None
        for i in range(n1):
            self.adi_pattern.append(PATTERN(n2,n3))
        self.centerfcm=[]
        for i in range(n3*n2):
            self.centerfcm.append(None)
    def Getdata(self,path,data_start,data_end):#读取样本
        data_path=path
        f=open(data_path,'r')
        lines=f.readlines()
        lines=[re.split('\s+',x) for x in lines]
        f.close()
        self.datas=[[float(y.strip()) for y in x[data_start:data_end]] for x in lines]
        rs=[x[-2] for x in lines]
        self.n_numpattern=len(self.datas)
        for i in range(self.n_numpattern):
            self.adi_pattern[i].a=self.datas[i]
            self.adi_pattern[i].r=rs[i]
            self.adi_pattern[i].id=i+1
            #print self.adi_pattern[i].a
    def Sortrry(self,an):#使单个样本中隶属度之和为1
        x=0
        bn=[]
        for i in range(len(an)):
            x+=an[i]
        if x==1:
            bn=an
        else:
            for i in range(len(an)):
                bn.append(float(an[i])/x)
        return bn
    def Inimatrixu(self):#随机初始化各个样本的隶属度
        bn=[]
        for i in range(self.n_numpattern*self.n_catacount):
            bn.append(None)
        for i in range(self.n_numpattern):
            for j in range(self.n_catacount):
                self.adi_pattern[i].b[j]=random.random()
            self.adi_pattern[i].b=self.Sortrry(self.adi_pattern[i].b)
        for i in range(self.n_numpattern):
            for j in range(self.n_catacount): 
                bn[i*self.n_catacount+j]=self.adi_pattern[i].b[j]
        return bn
    def Inicenter(self):#随机初始化各个类的中心值
        an=[]
        self.Inimatrixu()
        for i in range(self.n_catacount):
            for j in range(self.n_dimension):
                self.Centerfcm(i,j)
        return self.centerfcm
    def Distance(self,v1,v2,dimension):#两个数组的欧式距离
        result=0
        for i in range(dimension):
            result+=(v1[i]-v2[i])**2
        result=math.sqrt(result)
        return result
    def Objectfun(self):#此函数计算优化的目标函数
        center=[]
        objective=0
        for i in range(self.n_dimension):
            center.append(None)
        for i in range(self.n_catacount):
            for j in range(self.n_dimension):
                center[j]=self.centerfcm[i*self.n_dimension+j]
            for k in range(self.n_numpattern):
                objective+=math.pow(self.adi_pattern[k].b[i],self.f_weightm)*self.Distance(self.adi_pattern[k].a,center,self.n_dimension)**2
        return objective#返回类内加权平均误差和
    def Objectfunsingle(self,k):#评价单个样本的目标函数
        objective=0
        center=[]
        for i in range(self.n_dimension):
            center.append(None)
        for i in range(self.n_catacount):
            for j in range(self.n_dimension):
                center[j]=self.centerfcm[i*self.n_dimension+j]
            objective+=math.pow(self.adi_pattern[k].b[i],self.f_weightm)*self.Distance(self.adi_pattern[k].a,center,self.n_dimension)**2
        return objective

    def Matrixufcm(self,k,i):#求第k个样本对于第i个类得隶属度
        flagtemp=0
        f_temp=0
        for t in range(self.n_catacount):
            center=[]
            for j in range(self.n_dimension):
                center.append(self.centerfcm[t*self.n_dimension+j])
            if self.Distance(self.adi_pattern[k].a,center,self.n_dimension)>self.min_dis:
                f_temp+=math.pow(self.Distance(self.adi_pattern[k].a,center,self.n_dimension),-2.0/(self.f_weightm-1))#计算隶属度
            else:
                if t!=i:
                    flagtemp=1
        if flagtemp==1:
            self.adi_pattern[k].b[i]=0
            flagtemp=0
        else:
            center=[]
            for j in range(self.n_dimension):
                center.append(self.centerfcm[i*self.n_dimension+j])
            if self.Distance(self.adi_pattern[k].a,center,self.n_dimension)>self.min_dis:
                shit=math.pow(self.Distance(self.adi_pattern[k].a,center,self.n_dimension),-2.0/(self.f_weightm-1))
                self.adi_pattern[k].b[i]=shit/f_temp
            else:
                self.adi_pattern[k].b[i]=1
        return self.adi_pattern[k].b[i]
    def Centerfcm(self,i,j):#计算第i类j维的中心
        f_temp=0
        x=0
        #print i,' ',j
        for k in range(self.n_numpattern):
            f_temp+=math.pow(self.adi_pattern[k].b[i],self.f_weightm)*self.adi_pattern[k].a[j]
        x=f_temp
        f_temp=0
        for k in range(self.n_numpattern):
            f_temp+=math.pow(self.adi_pattern[k].b[i],self.f_weightm)
        x=x/f_temp
        self.centerfcm[i*self.n_dimension+j]=x
        return self.centerfcm[i*self.n_dimension+j]
    def Runfcm(self,n):#隶属度和聚类中心函数反复迭代
        for t in range(n):
            for i in range(self.n_catacount):
                for j in range(self.n_dimension):
                    self.Centerfcm(i,j)
            for k in range(self.n_numpattern):
                for i in range(self.n_catacount):
                    self.Matrixufcm(k,i)
    def GetCategorys(self):
        cats={}
        for i in range(self.n_catacount):
            cats[i]=[]
        for i in range(self.n_numpattern):
            index,max_value=GetListMaxIndex(self.adi_pattern[i].b)
            cats[index].append(i+1)
        return cats
    def Runmat(self,n):
        x=0
        t_start=now()
        self.Inimatrixu()
        self.Runfcm(n)
        x=self.Objectfun()
        t_end=now()
        t_time=t_end-t_start
        time=t_time
        print('time:',time)
        print('x:',x)
        return x
    def OutPutData(self):
        cats=self.GetCategorys()
        f=open('PF_FCM_result/fcm_result.txt','w+')
        dis_out_all=[]
        dis_in_all=[]
        c_keys=cats.keys()
        center=[]
        for i in range(self.n_catacount):
            
            c=[]
            for j in range(self.n_dimension):
                c.append(self.centerfcm[i*self.n_dimension+j])
            center.append(c)
            f.write('中心点：'+str(c)+'\n')
            f.write('分类结果：'+str(c))
            f.write(str(i)+'->'+str(cats[i])+'\n\n')
        
        for i in range(self.n_catacount):
            for j in range(i+1,self.n_catacount):
                dis_out_all.append(self.Distance(center[i],center[j],self.n_dimension))
        for c in cats.keys():
            cat=cats[c]
            cat_dis_all=[]
            for i in range(len(cat)):
                for j in range(i+1,len(cat)):
                    cat_dis_all.append(self.Distance(self.datas[cat[i]-1],self.datas[cat[j]-1],self.n_dimension))
            dis_in_all.append(sum(cat_dis_all)/len(cat_dis_all))
        dis_in_percent=sum(dis_in_all)/len(dis_in_all)
        dis_out_percent=sum(dis_out_all)/len(dis_out_all)
        f.write('类内平均距离：'+str(dis_in_percent)+'\t类间平均距离：'+str(dis_out_percent)+'\n\n')

        f.close()
        f=open('PF_FCM_result/fcm_yangben.txt','w+')
        for i in range(FCM.n_numpattern):
            f.write(str(i)+'\t'+str(FCM.adi_pattern[i].a)+'\t'+str(FCM.adi_pattern[i].b)+'\t'+FCM.adi_pattern[i].r+'\n')
        f.close()
