import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import xlrd
from sklearn.model_selection import train_test_split
#取数据
data=xlrd.open_workbook(r'数据准备表2.xlsx')
table=data.sheets()[6]
rowc=table.nrows
cols=table.ncols
arr=[]
for i in range(rowc):
    x=table.row_values(i)
    arr.append(x)
arr=np.array(arr)
x=arr[:,0:cols-1]
y=arr[:,cols-1:cols]

def weight_variable(shape):
    initial = tf.truncated_normal(shape,stddev=0.1)#生成一个截断的正态分布
    #initial =  tf.constant(0.015,shape=shape)
    return tf.Variable(initial)

#初始化偏置
def bias_variable(shape):
    initial = tf.constant(0.1,shape=shape)
    return tf.Variable(initial)

#卷积层
def conv2d(x,W):
    #x input tensor of shape `[batch, in_height, in_width, in_channels]`
    #W filter / kernel tensor of shape [filter_height, filter_width, in_channels, out_channels]
    #`strides[0] = strides[3] = 1`. strides[1]代表x方向的步长，strides[2]代表y方向的步长
    #padding: A `string` from: `"SAME", "VALID"`
    return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')

#池化层
def max_pool_2x2(x):
    #ksize [1,x,y,1]
    return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')


from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X = scaler.fit_transform(x)

from sklearn.preprocessing import OneHotEncoder
Y = OneHotEncoder().fit_transform(y).todense() #one-hot编码
batch_size = 50 # 使用MBGD算法，设定batch_size为109
print(x.shape,Y.shape)
X, X_test, Y, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
tf.reset_default_graph()

#定义两个placeholder
x = tf.placeholder(tf.float32,[None,200])#28*28
y = tf.placeholder(tf.float32,[None,2])

#改变x的格式转为4D的向量[batch, in_height, in_width, in_channels]`
x_image = tf.reshape(x,[-1,20,10,1])

#初始化第一个卷积层的权值和偏置
W_conv1 = weight_variable([3,3,1,32])#5*5的采样窗口，32个卷积核从1个平面抽取特征
b_conv1 = bias_variable([32])#每一个卷积核一个偏置值

#把x_image和权值向量进行卷积，再加上偏置值，然后应用于relu激活函数
di=conv2d(x_image,W_conv1)+ b_conv1
h_conv1 = tf.nn.relu(di)
#h_pool1 = max_pool_2x2(h_conv1)#进行max-pooling

#初始化第二个卷积层的权值和偏置
W_conv2 = weight_variable([2,2,32,32])#5*5的采样窗口，64个卷积核从32个平面抽取特征
b_conv2 = bias_variable([32])#每一个卷积核一个偏置值

#把h_pool1和权值向量进行卷积，再加上偏置值，然后应用于relu激活函数
h_conv2 = tf.nn.relu(conv2d(h_conv1,W_conv2) + b_conv2)
#h_pool2 = max_pool_2x2(h_conv2)#进行max-pooling

#28*28的图片第一次卷积后还是28*28，第一次池化后变为14*14
#第二次卷积后为14*14，第二次池化后变为了7*7
#进过上面操作后得到64张7*7的平面
'''
'''
#初始化第一个全连接层的权值
W_fc0 = weight_variable([20*10*32,32])#上一层有7*7*64个神经元，全连接层有1024个神经元
b_fc0 = bias_variable([32])#1024个节点
#把池化层2的输出扁平化为1维
h_pool2_flat = tf.reshape(h_conv2,[-1,20*10*32])
#求第一个全连接层的输出
h_fc0 = tf.nn.relu(tf.matmul(h_pool2_flat,W_fc0) + b_fc0)
'''
#单纯使用简单神经网络
x = tf.placeholder(tf.float32,[None,200])#28*28
y = tf.placeholder(tf.float32,[None,2])
W_fc0 = weight_variable([20*10,32])#上一层有7*7*64个神经元，全连接层有1024个神经元
b_fc0 = bias_variable([32])#1024个节点

h_fc0 = tf.nn.relu(tf.matmul(x,W_fc0) + b_fc0)
'''
W_fc1 = weight_variable([32,32])#上一层有7*7*64个神经元，全连接层有1024个神经元
b_fc1 = bias_variable([32])#1024个节点
h_fc1 = tf.nn.relu(tf.matmul(h_fc0,W_fc1) + b_fc1)



#keep_prob用来表示神经元的输出概率
keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1,keep_prob)

#初始化第个全连接层
W_fc2 = weight_variable([32,2])
b_fc2 = bias_variable([2])

#计算输出
prediction = tf.nn.softmax(tf.matmul(h_fc1_drop,W_fc2) + b_fc2)

#交叉熵代价函数
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=prediction)+tf.contrib.layers.l2_regularizer(0.03)(W_fc0)+tf.contrib.layers.l2_regularizer(0.03)(W_fc1)+tf.contrib.layers.l2_regularizer(0.03)(W_fc2))
#使用AdamOptimizer进行优化
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
#结果存放在一个布尔列表中
correct_prediction = tf.equal(tf.argmax(prediction,1),tf.argmax(y,1))#argmax返回一维张量中最大的值所在的位置
#求准确率
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
def generatebatch(X,Y,n_batch, batch_size,count):
        start = n_batch*batch_size
        end = start + batch_size
        if end>count:
            end=count
        #print(np.array(X[start:end]),1212,np.array(Y[start:end]))
        return np.array(X[start:end]),np.array(Y[start:end])
n_batch = Y.shape[0] // batch_size

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(400):
        for batch in range(n_batch):
            batch_xs, batch_ys = generatebatch(X,Y,batch,batch_size,Y.shape[0])
            sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys, keep_prob: 0.5})
        acc = sess.run(accuracy,feed_dict={x:X,y:Y,keep_prob:1.0})
        acc1 = sess.run(accuracy, feed_dict={x: X_test, y: Y_test, keep_prob: 1.0})
        print ("Iter " + str(epoch) + ", Training Accuracy= " + str(acc)+", Testing Accuracy= "+ str(acc1))

    conv1_16=sess.run(h_conv1,feed_dict={x: X}) #[397,20,10,32]
    print(conv1_16.shape)#
    conv1_reshape = sess.run(tf.reshape(conv1_16, [397, 32, 20, 10]))
    fig3, ax3 = plt.subplots(nrows=32, ncols=397, figsize=(397, 32))
    for i in range(3):
        ax3[i].imshow(conv1_reshape[i][0])
    plt.title('Conv1 16x28x28')
    plt.show()


        #1.本身该网络由卷积层1-》池化层1-》卷积层2-》池化层2-》全链接层1-》全连接层2-》输出层 组成，然而训练效果并不理想，在非过拟合基础上，测试集仅有不到70%正确率，我将两个池化层抽掉，正确率提高到了80%，与其他两个模型效果相似
#反卷积