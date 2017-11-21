#coding=utf-8
import numpy as np
import xlrd
import xlwt
import re
from numpy import int, int0
from builtins import int
import math

def add_dic(table,dic):
    rowc=table.nrows
    col=table.ncols
    for i in range(rowc):
        dic[table.row_values(i)[0]]=table.row_values(i)[1]
        #print(table.row_values(i)[0],table.row_values(i)[1])
    return dic
def add_dic2(table,dic):
    rowc=table.nrows
    col=table.ncols
    for i in range(rowc):
        dic[table.row_values(i)[0]]=table.row_values(i)[1]
        #print(table.row_values(i)[0],table.row_values(i)[1])
    return dic
def add_matix():
    medicine={}
    name={}
    data=xlrd.open_workbook(r'柴胡分析.xlsx')
    table=data.sheets()[1]
    name=add_dic(table, medicine)
    table=data.sheets()[2]
    medicine=add_dic(table, medicine)
    arr1=np.zeros((1066,373))
    arr2=np.ones((1066,373))
    table=data.sheets()[0]
    rowc=table.nrows
    for i in range(rowc):
        flag2=medicine.get(table.row_values(i)[2],-1)
        if flag2!=-1 and str(table.row_values(i)[3]).strip()!='':
            x=int(table.row_values(i)[0])-1
            y=int(medicine[table.row_values(i)[2]])
            #print(table.row_values(i)[0],str(table.row_values(i)[3]).strip())
            arr1[x,y] =math.log(float(str(table.row_values(i)[3]).strip()),math.e)
            arr2[x,y]=0
    return arr1,arr2
#arr1=add_matix()
#print(arr1)
def add_showdic():
    medicine={}
    name={}
    data=xlrd.open_workbook(r'柴胡分析.xlsx')
    table=data.sheets()[2]
    rowc=table.nrows
    col=table.ncols
    for i in range(rowc):
        medicine[int(table.row_values(i)[1])]=table.row_values(i)[0]
    table=data.sheets()[1]
    rowc=table.nrows
    col=table.ncols
    for i in range(rowc):
        name[int(table.row_values(i)[1])]=str(int(table.row_values(i)[1])+1)+' '+table.row_values(i)[0]
    return name,medicine