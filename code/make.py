import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(2,8)
data = pd.read_csv('data/d1.csv')
data=data[data['label']==0]
x = np.array(data[data.columns[:-1]])
for name in range(8):
    label = np.array(list(data[str(name)]))
    label2= np.array(list(data[str(name+1)]))
    ax[0][name].hist(label,bins=20,range=(0,30))
    #ax[0][name].scatter(label,label2)

data = pd.read_csv('result.csv')
# data=data[data['label']==0]
x = np.array(data[data.columns[:-1]])
for name in range(8):
    label = np.array(list(data[str(name)]))
    label2 = np.array(list(data[str(name + 1)]))
    ax[1][name].hist(label,bins=20,range=(0,30))
    #ax[1][name].scatter(label, label2)

plt.show()