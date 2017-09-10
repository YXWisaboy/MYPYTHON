from numpy import *
from PIL import Image
import operator
from os import listdir
#从列方向扩展
#tile(a,(size,1))
def knn(k,testdata,traindata,labels):
    #testdata:一维数组
    #traindata：二维数组
    #labels：一维列表，跟traindata一一对应
    #以下shape取的是训练数据的第一维，即其行数，也就是训练数据的个数
    traindatasize=traindata.shape[0]
    dif=tile(testdata,(traindatasize,1))-traindata
    #tile()的意思是给一维的测试数据转为与训练数据一样的行和列的格式
    #print(tile(testdata,(traindatasize,1)))
    sqdif=dif**2
    #axis=1-----》横向相加的意思
    sumsqdif=sqdif.sum(axis=1)
    #sumsqdif在此时已经成为1维的了
    distance=sumsqdif**0.5
    sortdistance=distance.argsort()
    #sortdistance为测试数据到各个训练数据的距离按近到远排序之后的结果
    count={}
    for i in range(0,k):
        vote=labels[sortdistance[i]]
        #sortdistance[i]测试数据最近的K个训练数据的下标
        #vote测试数据最近的K个训练数据的类别
        count[vote]=count.get(vote,0)+1
    sortcount=sorted(count.items(),key=operator.itemgetter(1),reverse=True)
    return sortcount[0][0]


#图片处理
#先将所有图片转为固定宽高，比如32*32，然后再转为文本
#pillow
im=Image.open("C:/Users/me/Pictures/weixin3.jpg")
fh=open("C:/Users/me/Pictures/weixin3.txt","a")
#im.save("C:/Users/me/Pictures/weixin.bmp")
width=im.size[0]
height=im.size[1]
#k=im.getpixel((1,9))
#print(k)
for i in range(0,width):
    for j in range(0,height):
        cl=im.getpixel((i,j))
        clall=cl[0]+cl[1]+cl[2]
        if(clall==0):
            #黑色
            fh.write("1")
        else:
            fh.write("0")
    fh.write("\n")
fh.close()

#加载数据
def datatoarray(fname):
    arr=[]
    fh=open(fname)
    for i in range(0,32):
        thisline=fh.readline()
        for j in range(0,32):
            arr.append(int(thisline[j]))
    return arr
arr1=datatoarray("D:/Python35/traindata/0_4.txt")
#print(arr1)
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
        trainarr[i,:]=datatoarray("traindata/"+thisfname)
    return trainarr,labels
#用测试数据调用KNN算法去测试，看是否能够准确识别
def datatest():
    trainarr,labels=traindata()
    testlist=listdir("testdata")
    tnum=len(testlist)
    for i in range(0,tnum):
        thistestfile=testlist[i]
        testarr=datatoarray("testdata/"+thistestfile)
        rknn=knn(3,testarr,trainarr,labels)
        print(rknn)
#datatest()
#抽某一个测试文件出来进行试验
trainarr,labels=traindata()
thistestfile="8_76.txt"
testarr=datatoarray("testdata/"+thistestfile)
#print(testarr)
rknn=knn(3,testarr,trainarr,labels)
print(rknn)
