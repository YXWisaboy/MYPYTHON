# -*- coding: utf-8 -*-
import sugartensor as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
__author__ = 'buriburisuri@gmail.com'

# set log level to debug
tf.sg_verbosity(10)

#
# hyper parameters
#

batch_size = 100  # batch size
num_category = 2  # total categorical factor
num_cont = 2  # total continuous factor
num_dim = 50  # total latent dimension

#
# inputs
#

# target_number
target_num = tf.placeholder(dtype=tf.sg_intx, shape=batch_size)
# target continuous variable # 1
target_cval_1 = tf.placeholder(dtype=tf.sg_floatx, shape=batch_size)
# target continuous variable # 2
target_cval_2 = tf.placeholder(dtype=tf.sg_floatx, shape=batch_size)

# category variables
z = (tf.ones(batch_size, dtype=tf.sg_intx) * target_num).sg_one_hot(depth=num_category)

# continuous variables
z = z.sg_concat(target=[target_cval_1.sg_expand_dims(), target_cval_2.sg_expand_dims()])

# random seed = categorical variable + continuous variable + random uniform
z = z.sg_concat(target=tf.random_uniform((batch_size, num_dim-num_category-num_cont)))

#
# create generator
#

# generator network
with tf.sg_context(name='generator', stride=2, act='relu', bn=True):
    # gen = (z.sg_dense(dim=1024)
    #        .sg_dense(dim=7 * 7 * 128)
    #        .sg_reshape(shape=(-1, 7, 7, 128))
    #        .sg_upconv(size=4, dim=64)
    #        .sg_upconv(size=4, dim=1, act='sigmoid', bn=False).sg_squeeze())

#
# run generator
    gen = (z.sg_dense(dim=60)
           .sg_dense(dim=190)
           .sg_dense(dim=190)
           )
           # .sg_reshape(shape=(-1, 7, 7, 128))
           # .sg_upconv(size=4, dim=64)
           # .sg_upconv(size=4, dim=1, act='sigmoid', bn=False


maxvalue=0

def run_generator(num, x1, x2, dir):
    arr = []
    with tf.Session() as sess:
        tf.sg_init(sess)
        # restore parameters
        saver = tf.train.Saver()
        saver.restore(sess, tf.train.latest_checkpoint('asset/train/'))

        # run generator
        imgs = sess.run(gen, {target_num: num,
                              target_cval_1: x1,
                              target_cval_2: x2})
        print(imgs)
        # pd.DataFrame(imgs).to_csv(dir)
        varlist=np.round(np.std(imgs,axis=0))
        return varlist
        # pd.DataFrame(varlist).to_csv('result.csv')
        # print('num:',num)
        # print('num1:',sess.run((tf.ones(batch_size, dtype=tf.sg_intx) * target_num).sg_one_hot(depth=num_category).\
        #                        sg_concat(target=[target_cval_1.sg_expand_dims(), target_cval_2.sg_expand_dims()]),\
        #                        feed_dict={target_num: num,
        #                       target_cval_1: x1,
        #                       target_cval_2: x2}))
        # plot result

        # for i in range(10):
        #     for j in range(10):
        #         ax[i][j].imshow(imgs[i * 10 + j], 'gray')
        #         ax[i][j].set_axis_off()
        #1.for image show
        # _, ax = plt.subplots()
        # for i in range(10):
        #     for j in range(10):
        #         # print('i=',i,' j=',j,'result=',imgs[i * 10 + j])
        #         nowimg=imgs[i * 10 + j]
        #         valuemax=max(valuemax,max(nowimg))
        #         arr.append(np.hstack((nowimg, [0] * 10)).reshape(10, 20))
        #
        # for i in range(10):
        #     for j in range(10):
        #         print(i,j)
        #         a=sns.heatmap(pd.DataFrame(np.round(arr[i * 10 + j], 3), columns=range(20), index=range(10)),
        #                     annot=False, vmax=5, vmin=0, xticklabels=True, yticklabels=True, square=False, cmap="YlGnBu",cbar=False)
        #         # print(a)
        #         ax=a
        #         plt.savefig('asset/train/picture' +str(i)+','+str(j))
        #         # plt.show()

# draw sample by categorical division
#

# # fake image
# run_generator(np.random.randint(0, num_category, batch_size),
#               np.random.uniform(0, 1, batch_size), np.random.uniform(0, 1, batch_size),
#               fig_name='fake.png')
#
# # classified image
# run_generator(np.arange(10).repeat(10), np.ones(batch_size) * 0.5, np.ones(batch_size) * 0.5)

#
# draw sample by continuous division
#
arr=[]
for j in range(4):
    i=1
    var1=run_generator(np.ones(batch_size) * i,
                  # np.linspace(0, 1, 10).repeat(10),
                  # np.expand_dims(np.linspace(0, 1, 10), axis=1).repeat(10, axis=1).T.flatten(),
                np.ones(100) * 0.1,
                np.linspace(0, 1, 100),
                dir='result.csv'
    )

    var2=run_generator(np.ones(batch_size) * i,
                  # np.linspace(0, 1, 10).repeat(10),
                  # np.expand_dims(np.linspace(0, 1, 10), axis=1).repeat(10, axis=1).T.flatten(),
                np.linspace(0, 1, 100),
                np.ones(100) * 0.1,
                dir='result1.csv'
    )
    li=var1-var2
    arr.append(li)
    plt.subplot(411+j)
    plt.plot(range(190),li)
    plt.xticks(range(0,190,10))
    plt.xlabel('featureid')
    plt.ylabel('var1-var2')

pd.DataFrame(arr).to_csv('var.csv')
plt.show()







