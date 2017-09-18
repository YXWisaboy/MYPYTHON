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
def add_matix():
    medicine={}
    reason={}
    data=xlrd.open_workbook(r'字典索引.xlsx')
    table=data.sheets()[0]
    reason1=add_dic(table, medicine)
    table=data.sheets()[1]
    reason1=add_dic(table, reason)
    arr1=np.zeros((12,43,190))
    arr2=np.ones((12,43,190))
    arr3=np.ones((12,43,190))
    data=xlrd.open_workbook(r'test.xls')
    table=data.sheets()[0]
    rowc=table.nrows
    for i in range(rowc):
        flag1=reason.get(table.row_values(i)[2],0)
        flag2=medicine.get(table.row_values(i)[4],0)
        if flag1!=0 and flag2!=0:
            x=int(table.row_values(i)[1])-1
            y=int(reason[table.row_values(i)[2]])
            z=int(medicine[table.row_values(i)[4]])
            arr1[x,y,z] =float(table.row_values(i)[5])+arr1[x,y,z]
            arr2[x,y,z] =arr2[x,y,z]+1
            arr3[x,y,z]=0
    for i in range(np.size(arr2, 0)):
        for j in range(np.size(arr2, 1)):
            for y in range(np.size(arr2, 2)):
                if arr2[i,j,y]!=1:
                    arr2[i,j,y]-=1
    arr1=np.divide(arr1,arr2)
    return arr1,arr2,arr3
arr1=add_matix()

def add_showdic():
    medicine={}
    reason={}
    data=xlrd.open_workbook(r'字典索引.xlsx')
    table=data.sheets()[0]
    rowc=table.nrows
    col=table.ncols
    for i in range(rowc):
        medicine[int(table.row_values(i)[1])]=table.row_values(i)[0]
    table=data.sheets()[1]
    rowc=table.nrows
    col=table.ncols
    for i in range(rowc):
        reason[int(table.row_values(i)[1])]=table.row_values(i)[0]
    return reason,medicine