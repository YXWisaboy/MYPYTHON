#贝叶斯算法的应用
from numpy import *
import operator
from os import listdir
import numpy as npy
import numpy
class Bayes:
    def __init__(self):
        self.length=-1
        self.labelcount=dict()#各类别的概率{"类别1"：概率1，"类别2"：概率2,…}
        self.vectorcount=dict()#以字典的方式存储类别与特征向量，
        #格式为{"类别1":[特征向量1,特征向量2,…],…,"类别n":[特征向量1,特征向量2,…]}
    def fit(self,dataSet:list,labels:list):
        if(len(dataSet)!=len(labels)):
            raise ValueError("您输入的训练数组跟类别数组长度不一致")
        self.length=len(dataSet[0])#测试数据特征值的长度
        labelsnum=len(labels)#类别所有的数量（可重复）
        norlabels=set(labels)#不重复类别的数量
        for item in norlabels:
            thislabel=item
            self.labelcount[thislabel]=labels.count(thislabel)/labelsnum#求的当前类别占类别总数的比例，p(c)
        #通过zip将两个数组交叉放置，比如：
        '''
        x1=[a,b,c]
        x2=[e,f,g]
        k=zip(x1,x2)
        k:[(a,e),(b,f),(c,g)]
        '''
        for vector,label in zip(dataSet,labels):
            if(label not in self.vectorcount):
                self.vectorcount[label]=[]
            self.vectorcount[label].append(vector)
        print("训练结束")
        return self
    def btest(self,TestData,labelsSet):
        if(self.length==-1):
            raise ValueError("您还没有进行训练，请先训练")
        #计算testdata分别为各个类别的概率
        lbDict=dict()#{"类别1"：概率1，“类别2”：概率2}
        for thislb in labelsSet:
            p=1
            alllabel=self.labelcount[thislb]#当前类别的概率p(c)
            allvector=self.vectorcount[thislb]#当前类别的所有特征向量
            vnum=len(allvector)#当前类别特征向量个数
            allvector=numpy.array(allvector).T#转置一下
            #如
            '''
            原来的是[[t1,t2,t3,t4],[t1,t2,t3,t4]]
            现在成为：[t1,t1],[t2,t2]……[t4,t4]
            '''
            for index in range(0,len(TestData)):#依次计算各特征的概率
                vector=list(allvector[index])
                p*=vector.count(TestData[index])/vnum#p(当前特征|C)
                #如testdata[0]:0,vector:[1,0,1,0,0,1,1],p为3/7
            lbDict[thislb]=p*alllabel#alllabel相当于p(c)
        thislabel=sorted(lbDict,key=lambda x:lbDict[x],reverse=True)[0]
        return thislabel

#加载数据
def datatoarray(fname):
    arr=[]
    fh=open(fname)
    for i in range(0,32):
        thisline=fh.readline()
        for j in range(0,32):
            arr.append(int(thisline[j]))
    return arr
#建立一个函数取文件名前缀
def seplabel(fname):
    filestr=fname.split(".")[0]
    label=int(filestr.split("_")[0])
    return label
#建立训练数据
def traindata():
    labels=[]
    trainfile=listdir("D:/Python35/traindata")
    num=len(trainfile)
    #长度1024（列），每一行存储一个文件
    #用一个数组存储所有训练数据，行：文件总数，列：1024
    trainarr=zeros((num,1024))
    for i in range(0,num):
        thisfname=trainfile[i]
        thislabel=seplabel(thisfname)
        labels.append(thislabel)
        trainarr[i,:]=datatoarray("D:/Python35/traindata/"+thisfname)
    return trainarr,labels
bys=Bayes()
#训练数据
train_data,labels=traindata()
bys.fit(train_data,labels)
#测试
thisdata=datatoarray("D:/Python35/testdata/8_90.txt")
labelsall=[0,1,2,3,4,5,6,7,8,9]
#识别单个手写体数字
'''
rst=bys.btest(thisdata,labelsall)
print(rst)
'''
#识别多个手写体数字（批量测试）
testfileall=listdir("D:/Python35/testdata")
num=len(testfileall)
x=0
for i in range(0,num):
    thisfilename=testfileall[i]
    thislabel=seplabel(thisfilename)
    #print(thislabel)
    thisdataarray=datatoarray("D:/Python35/testdata/"+thisfilename)
    label=bys.btest(thisdataarray,labelsall)
    print("该数字是:"+str(thislabel)+",识别出来的数字是："+str(label))
    if(label!=thislabel):
        x+=1
        print("此次出错")
print(x)
print("错误率是："+str(float(x)/float(num)))
