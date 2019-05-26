import sugartensor as tf
import numpy as np
import pandas as pd
from tensorflow.examples.tutorials.mnist import input_data

reshape=False
one_hot=False
data_set = input_data.read_data_sets('./asset/data/mnist', reshape=reshape, one_hot=one_hot)
print(data_set.train.images.shape)
print(data_set.train.labels.shape)
data = pd.read_csv('data/d1.csv')
x = np.array(data[data.columns[:-1]])
label = np.array(list(data['label']))
print(x.shape)
print(label.shape)