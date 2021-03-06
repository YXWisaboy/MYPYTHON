
#!/usr/bin/env python
# coding: UTF-8
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import xlrd
import xlwt
from sklearn import datasets, linear_model
#r'C:\Users\sjzx\Desktop\工作簿1.xlsx'
def get_data(file_name):
    data=xlrd.open_workbook(file_name)
    table=data.sheets()[0]
    PM = []
    TEMP = []
    count=0
    for i in zip(table.col_values(7),table.col_values(5)):
        Temp,pm=i[0],i[1]
        try:
            if count==0:
                count=1
                continue
            if pm=='NA':
                continue
            PM.append(float(pm))
            TEMP.append([float(Temp)])
        except:
            pass
        else:
            pass
    return TEMP,PM

def linear_model_main(X_parameters,Y_parameters,predict_value):
     regr = linear_model.LinearRegression()
     regr.fit(X_parameters, Y_parameters)
     predict_outcome = regr.predict(predict_value)
     predictions = {}
     predictions['intercept'] = regr.intercept_
     predictions['coefficient'] = regr.coef_
     predictions['predicted_value'] = predict_outcome
     return predictions
 
def show_linear_line(X_parameters,Y_parameters):
 # Create linear regression object
     regr = linear_model.LinearRegression()
     regr.fit(X_parameters, Y_parameters)
     plt.scatter(X_parameters,Y_parameters,color='blue')
     plt.plot(X_parameters,regr.predict(X_parameters),color='red',linewidth=4)
     plt.xticks(('温度'))
     plt.yticks(('PM'))
     plt.show()
     
X,Y = get_data(r'C:\Users\sjzx\Desktop\工作簿1.xlsx')
predictvalue = 3
result = linear_model_main(X,Y,predictvalue)
print("Intercept value ", result['intercept'])
print("coefficient", result['coefficient'])
print("Predicted value: ",result['predicted_value'])
show_linear_line(X,Y)