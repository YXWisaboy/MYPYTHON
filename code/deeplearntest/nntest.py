from keras.models import Sequential
from keras.layers import Dense, Activation
import csv
import random
import numpy as np
import keras.utils
def loadCsv(filename):
    lines = csv.reader(open(filename, "r"))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]
    return dataset

def splitDataset(dataset, splitRatio):
    trainSize = int(len(dataset) * splitRatio)
    trainSet = []
    copy = list(dataset)
    while len(trainSet) < trainSize:
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))
    return trainSet, copy
def separateByClass(dataset):
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        if (vector[-1] not in separated):
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    return separated
filename = r'逻辑回归训练集.csv'
splitRatio = 0.67
dataset = loadCsv(filename)
trainingSet, testSet = splitDataset(dataset, splitRatio)
x_train=np.array(trainingSet)[:,0:-1]
y_train=np.array(trainingSet)[:,-1]
y_train = keras.utils.to_categorical(y_train, num_classes=2)
x_test=np.array(testSet)[:,0:-1]
y_test=np.array(testSet)[:,-1]
y_test = keras.utils.to_categorical(y_test, num_classes=2)

model = Sequential()
model.add(Dense(32, input_shape=(8,)))
model.add(Activation('sigmoid'))
model.add(Dense(32))
model.add(Activation('sigmoid'))
model.add(Dense(2))
model.add(Activation('softmax'))
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
model.fit(x_train, y_train,epochs=20,batch_size=128)
score = model.evaluate(x_test, y_test, batch_size=128)
print(score)