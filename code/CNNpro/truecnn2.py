
import tensorflow as tf
import numpy as np
import xlrd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder
import random

def generatebatch(X, Y, n_batch, batch_size, count):
    #顺序打乱
    #index=range(len(Y))
    index=np.random.permutation(len(Y))
    X_NEW=X[index]
    Y_NEW=Y[index]
    start = n_batch * batch_size
    end = start + batch_size
    if end > count:
        end = count
    # print(np.array(X[start:end]),1212,np.array(Y[start:end]))
    return np.array(X_NEW[start:end]), np.array(Y_NEW[start:end])
def deletecol(list,x1):
    #将指定行列置为0
    for i in list:
        x1[:,i]=0

def weight_variable(shape,name=''):
    initial = tf.truncated_normal(shape,stddev=0.1)#生成一个截断的正态分布
    #initial = tf.constant(0.0025, shape=shape)#生成常数分布
    if name != '':
        return tf.Variable(initial,name=name)
    else:
        return tf.Variable(initial)

#初始化偏置
def bias_variable(shape):
    initial = tf.constant(0.1,shape=shape)
    return tf.Variable(initial)




def nn(sumlist):
    data = xlrd.open_workbook(r'数据准备表2.xlsx')
    table = data.sheets()[6]
    rowc = table.nrows
    cols = table.ncols
    arr = []
    for i in range(rowc):
        x = table.row_values(i)
        arr.append(x)
    arr = np.array(arr)
    define()
    for m in sumlist:
        maincount(arr, cols,m)


def maincount(arr,cols,m):
    #取数据
    arr1=arr-0
    x = arr1[:, 0:cols - 1]
    y = arr1[:, cols - 1:cols]

    scaler = MinMaxScaler()
    #X = scaler.fit_transform(x)
    X=x
    #print(X.shape,X)

    Y = OneHotEncoder().fit_transform(y).todense() #one-hot编码
    batch_size = 50 # 使用MBGD算法，设定batch_size为109
    A = Y.sum(axis=0)[0,0]
    B = Y.sum(axis=0)[0, 1]

    cha=abs(A-B)
    if A<B:
        flag=0
    else:
        flag=1
    count=0
    while count==cha:
        a=random.randint(0,len(y))
        if y[a][flag]==1:
            X.append(X[a])
            Y.append(Y[a])
            count+=1

    deletecol(m,X)

    X, X_test, Y, Y_test = train_test_split(X, Y, test_size=0.25, random_state=0)
    tf.reset_default_graph()

    #单纯使用简单神经网络
    x = tf.placeholder(tf.float32,[None,200])#28*28
    y = tf.placeholder(tf.float32,[None,2])
    W_fc0 = weight_variable([20*10,32],name='w0')#上一层有7*7*64个神经元，全连接层有1024个神经元
    b_fc0 = bias_variable([32])#1024个节点

    h_fc0 = tf.nn.relu(tf.matmul(x,W_fc0) + b_fc0)
    W_fc1 = weight_variable([32,32],name='w1')#上一层有7*7*64个神经元，全连接层有1024个神经元
    b_fc1 = bias_variable([32])#1024个节点
    h_fc1 = tf.nn.relu(tf.matmul(h_fc0,W_fc1) + b_fc1)

    #keep_prob用来表示神经元的输出概率
    keep_prob = tf.placeholder(tf.float32)
    h_fc1_drop = tf.nn.dropout(h_fc1,keep_prob)

    #初始化第个全连接层
    W_fc2 = weight_variable([32,2],name='w2')
    b_fc2 = bias_variable([2])

    #计算输出
    prediction = tf.nn.softmax(tf.matmul(h_fc1_drop,W_fc2) + b_fc2)
    #缓存初始权值

    #交叉熵代价函数
    ss=0.025
    cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=prediction)+tf.contrib.layers.l2_regularizer(ss)(W_fc0)+tf.contrib.layers.l2_regularizer(ss)(W_fc1)+tf.contrib.layers.l2_regularizer(ss)(W_fc2))
    #使用AdamOptimizer进行优化
    train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
    #结果存放在一个布尔列表中
    correct_prediction = tf.equal(tf.argmax(prediction,1),tf.argmax(y,1))#argmax返回一维张量中最大的值所在的位置
    #求准确率
    accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

    # 以下为召回率、精确率、F1等的计算
    predictions = tf.argmax(prediction, 1)
    actuals = tf.argmax(y, 1)
    ones_like_actuals = tf.ones_like(actuals)
    zeros_like_actuals = tf.zeros_like(actuals)
    ones_like_predictions = tf.ones_like(predictions)
    zeros_like_predictions = tf.zeros_like(predictions)
    tp_op = tf.reduce_sum(
        tf.cast(
            tf.logical_and(
                tf.equal(actuals, ones_like_actuals),
                tf.equal(predictions, ones_like_predictions)
            ),
            "float"
        )
    )
    tn_op = tf.reduce_sum(
        tf.cast(
            tf.logical_and(
                tf.equal(actuals, zeros_like_actuals),
                tf.equal(predictions, zeros_like_predictions)
            ),
            "float"
        )
    )
    fp_op = tf.reduce_sum(
        tf.cast(
            tf.logical_and(
                tf.equal(actuals, zeros_like_actuals),
                tf.equal(predictions, ones_like_predictions)
            ),
            "float"
        )
    )
    fn_op = tf.reduce_sum(
        tf.cast(
            tf.logical_and(
                tf.equal(actuals, ones_like_actuals),
                tf.equal(predictions, zeros_like_predictions)
            ),
            "float"
        )
    )

    n_batch = Y.shape[0] // batch_size
    saver1=tf.train.Saver([W_fc0,W_fc1,W_fc2])
    with tf.Session() as sess:
        list1=[]
        list2=[]
        list3=[]
        list4=[]
        list5 = []
        #sess.run(tf.global_variables_initializer())
        saver1.restore(sess,'./seed1')
        sess.run(b_fc0.initializer)
        sess.run(b_fc1.initializer)
        sess.run(b_fc2.initializer)
        for epoch in range(2000):
            for batch in range(n_batch):
                batch_xs, batch_ys = generatebatch(X,Y,batch,batch_size,Y.shape[0])
                sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys, keep_prob: 0.5})
            acc = sess.run(accuracy,feed_dict={x:X,y:Y,keep_prob:1.0})
            acc1 = sess.run(accuracy, feed_dict={x: X_test, y: Y_test, keep_prob: 1.0})
            list1.append(acc1)
            # print ("Iter " + str(epoch) + ", Training Accuracy= " + str(acc)+", Testing Accuracy= "+ str(acc1))

            #以下为召回率、精确率、F1等的计算
            #print(sess.run(predictions,feed_dict={x:X,y:Y,keep_prob:1.0}))
            #print(sess.run(actuals, feed_dict={x: X, y: Y, keep_prob: 1.0}))
            tp, tn, fp, fn = \
                sess.run(
                    [tp_op, tn_op, fp_op, fn_op],
                    #feed_dict={x:X,y:Y,keep_prob:1.0}
                    feed_dict = {x: X_test, y: Y_test, keep_prob: 0.7}
                )
            if tp==0 or tn==0 or fp==0 or fn==0:
                pass
                #print(str(epoch),tp, tn, fp, fn)
            else:
                tpr = float(tp) / (float(tp) + float(fn))
                fpr = float(fp) / (float(tp) + float(fn))
                accuracynum = (float(tp) + float(tn)) / (float(tp) + float(fp) + float(fn) + float(tn))
                list2.append(accuracynum)
                recall = tpr
                list3.append(recall)
                precisionnum = float(tp) / (float(tp) + float(fp))
                list4.append(precisionnum)
                f1_score = (2 * (precisionnum * recall)) / (precisionnum + recall)
                list5.append(f1_score)
                #print ("Iter " + str(epoch) + ", Training Accuracy= " + str(acc)+", Testing Accuracy= "+ str(acc1))
                #print( str(epoch),'Precision = ', precisionnum,' Recall = ', recall,' F1 Score = ', f1_score,' Accuracy = ', accuracynum)

        print(m,'预测最大值为：',max(list1),',accracy:',max(list2),',recall:',max(list3),',precision:',max(list4),',f1:',max(list5))



def define():
    W_fc0 = weight_variable([20 * 10, 32], name='w0')  # 上一层有7*7*64个神经元，全连接层有1024个神经元
    b_fc0 = bias_variable([32])  # 1024个节点
    W_fc1 = weight_variable([32, 32], name='w1')  # 上一层有7*7*64个神经元，全连接层有1024个神经元
    b_fc1 = bias_variable([32])  # 1024个节点
    W_fc2 = weight_variable([32, 2], name='w2')
    b_fc2 = bias_variable([2])
    saver=tf.train.Saver()
    with tf.Session() as sess:
        init_op=tf.global_variables_initializer()
        sess.run(init_op)
        saver.save(sess,'./seed1',global_step=1)

def dataready():
    data = xlrd.open_workbook(r'数据准备表2.xlsx')
    table = data.sheets()[8]
    rowc = table.nrows
    cols = table.ncols
    arr = []
    for i in range(rowc):
        e=[]
        for j in range(cols):
            if table.row_values(i)[j]!='':
                e.append(int(table.row_values(i)[j]))
        arr.append(e)
    return arr
#计算药物类列表
def DBscan():
    from sklearn.cluster import KMeans
    from sklearn.preprocessing import StandardScaler
    data = xlrd.open_workbook(r'数据准备表3（聚类）.xlsx')
    table = data.sheets()[0]
    rowc = table.nrows
    cols = table.ncols
    arr = []
    for i in range(rowc):
        x = table.row_values(i)
        arr.append(x)
    arr = np.array(arr)
    # data = StandardScaler().fit_transform(arr)
    #print(arr[180])
    model = KMeans(n_clusters=7, init='k-means++', n_init=5)
    y_pred = list(model.fit_predict(arr))
    #print(y_pred)
    # model = DBSCAN(eps=50, min_samples=6)
    # model.fit(arr)
    # y= model.labels_
    # print(y)
    dic = {}
    list1=[[],[]]
    for i in range(len(y_pred)):
        dic.setdefault(y_pred[i], [])
        dic[y_pred[i]].append(i)
    for i in dic.keys():
        list1.append(dic[i])
    return list1
#nn([[]])
print('----------------------')
#nn(dataready())
print('----------------------')
nn(DBscan())

#在该算法中我尝试了L2正则化，可以有效提高测试机准确率，但是无论无何调整都无法大于0.81，并且在测试机准确率较高的时候，训练集准确率也是约80%，所以我怀疑该数据本身就有着约10%的人工错误率