#coding=utf-8
import numpy as np
import xlrd
import xlwt
import re
from numpy import int, int0
from builtins import int

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
    reason={}
    data=xlrd.open_workbook(r'字典索引.xlsx')
    table=data.sheets()[0]
    reason1=add_dic(table, medicine)
    arr1=np.zeros((1090,190))
    arr2=np.ones((1090,190))
    data=xlrd.open_workbook(r'去空后的计量表.xls')
    table=data.sheets()[0]
    rowc=table.nrows
    for i in range(rowc):
        flag2=medicine.get(table.row_values(i)[5],0)
        if flag2!=0:
            x=int(table.row_values(i)[0])
            y=int(medicine[table.row_values(i)[5]])
            arr1[x,y] =float(table.row_values(i)[6])
            arr2[x,y]=0
    return arr1,arr2
#arr1=add_matix()
#print(arr1)
def add_showdic():
    medicine={}
    reason={}
    data=xlrd.open_workbook(r'字典索引.xlsx')
    table=data.sheets()[0]
    rowc=table.nrows
    col=table.ncols
    for i in range(rowc):
        medicine[int(table.row_values(i)[1])]=table.row_values(i)[0]
    table=data.sheets()[2]
    rowc=table.nrows
    col=table.ncols
    for i in range(rowc):
        reason[int(table.row_values(i)[2])]=table.row_values(i)[0]+' '+table.row_values(i)[1]
    return reason,medicine