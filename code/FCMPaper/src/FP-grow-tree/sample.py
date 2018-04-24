#-*- coding:utf-8 –*-
import xlrd
import FP_Grow_tree

def add_matix():
    data=xlrd.open_workbook(r'D:\YXW.FILE\code\FCMPaper\src\方剂横向表.xls')
    table=data.sheets()[0]
    arr=[]
    list=[]
    rowc=table.nrows
    for i in range(rowc):
    	for j in table.row_values(i):
    		if j!='':
    			list.append(j)
    	arr.append(list)
    	list=[]
    return arr

sample=[
	['milk','eggs','bread','chips'],
	['eggs','popcorn','chips','beer'],
	['eggs','bread','chips'],
	['milk','eggs','bread','popcorn','chips','beer'],
	['milk','bread','beer'],
	['eggs','bread','beer'],
	['milk','bread','chips'],
	['milk','eggs','bread','butter','chips'],
	['milk','eggs','butter','chips']
]
sample2 = [['r', 'z', 'h', 'j', 'p'],
               ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
               ['z'],
               ['r', 'x', 'n', 'o', 's'],
               ['y', 'r', 'x', 'z', 'q', 't', 'p'],
               ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]
sample1=[
	[u'牛奶',u'鸡蛋',u'面包',u'薯片'],
	[u'鸡蛋',u'爆米花',u'薯片',u'啤酒'],
	[u'鸡蛋',u'面包',u'薯片'],
	[u'牛奶',u'鸡蛋',u'面包',u'爆米花',u'薯片',u'啤酒'],
	[u'牛奶',u'面包',u'啤酒'],
	[u'鸡蛋',u'面包',u'啤酒'],
	[u'牛奶',u'面包',u'薯片'],
	[u'牛奶',u'鸡蛋',u'面包',u'黄油',u'薯片'],
	[u'牛奶',u'鸡蛋',u'黄油',u'薯片']
]

sample3=add_matix()
#print(sample1)
##参数说明 sample为事务数据集 []为递归过程中的基,support为最小支持度
for i in range(400,600):

    support=i
    ff=FP_Grow_tree.FP_Grow_tree(sample3,[],support)
    ##打印频繁集
    #ff.printfrequent()
    #ff.printconfident(0.9)
    ff.printcount()
