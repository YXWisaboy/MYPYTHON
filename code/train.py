# -*- coding: utf-8 -*-
import sugartensor as tf
import numpy as np
import pandas as pd
__author__ = 'buriburisuri@gmail.com'


# set log level to debug
tf.sg_verbosity(10)

#
# hyper parameters
#

# batch_size = 32   # batch size
# num_category = 10  # total categorical factor
# num_cont = 2  # total continuous factor
# num_dim = 50  # total latent dimension
#d1
batch_size = 10   # batch size
num_category = 2  # total categorical factor
num_cont = 2  # total continuous factor
num_dim = 50  # total latent dimension
#
# inputs
#
def _data_to_tensor(data_list, batch_size, name=None):
    r"""Returns batch queues from the whole data.

    Args:
      data_list: A list of ndarrays. Every array must have the same size in the first dimension.
      batch_size: An integer.
      name: A name for the operations (optional).

    Returns:
      A list of tensors of `batch_size`.
    """
    # convert to constant tensor
    const_list = [tf.constant(data) for data in data_list]

    # create queue from constant tensor
    queue_list = tf.train.slice_input_producer(const_list, capacity=batch_size * 10, name=name)

    # create batch queue
    return tf.train.shuffle_batch(queue_list, batch_size, capacity=batch_size * 10,
                                  min_after_dequeue=batch_size * 1, name=name)
class Mnist(object):
    def __init__(self, batch_size=10, reshape=False, one_hot=False):
        data = pd.read_csv('data/d1.csv')
        x = np.array(data[data.columns[:-1]])
        label = np.array(list(data['label']))
        # load sg_data set
        self.batch_size = batch_size

        # member initialize
        self.train= tf.sg_opt()

        # convert to tensor queue
        self.train.image, self.train.label = \
            _data_to_tensor([x.astype('float32'), label.astype('int32')], batch_size, name='train')

        # calc total batch count
        self.train.num_batch = label.shape[0] // batch_size

# MNIST input tensor ( with QueueRunner )
data = Mnist(batch_size=batch_size)
# input images
x = data.train.image
# generator labels ( all ones )
y = tf.ones(batch_size, dtype=tf.sg_floatx)
# discriminator labels ( half 1s, half 0s )
y_disc = tf.concat( [y, y * 0],0)
#
# create generator
#
# random class number
z_cat = tf.multinomial(tf.ones((batch_size, num_category), dtype=tf.sg_floatx) / num_category, 1).sg_squeeze().sg_int()
# random seed = random categorical variable + random uniform
z = z_cat.sg_one_hot(depth=num_category).sg_concat(target=tf.random_uniform((batch_size, num_dim-num_category)))
# random continuous variable
z_cont = z[:, num_category:num_category+num_cont]
# category label
label = tf.concat([data.train.label, z_cat],0)
# generator network
with tf.sg_context(name='generator', size=4, stride=2, act='relu', bn=True):
    # gen = (z.sg_dense(dim=1024)
    #        .sg_dense(dim=7*7*128)
    #        .sg_reshape(shape=(-1, 7, 7, 128))
    #        .sg_upconv(dim=64)
    #        .sg_upconv(dim=1, act='sigmoid', bn=False))
#d1
    gen = (z.sg_dense(dim=60)
           .sg_dense(dim=190)
           .sg_dense(dim=190)
           )
# add image summary
# tf.sg_summary_image(gen)

#
# create discriminator & recognizer
#
print(x,gen)
# create real + fake image input
xx = tf.concat([x, gen],0)

with tf.sg_context(name='discriminator', size=4, stride=2, act='leaky_relu'):
    # shared part
    # shared = (xx.sg_conv(dim=64)
    #           .sg_conv(dim=128)
    #           .sg_flatten()
    #           .sg_dense(dim=1024))
    #d1
    shared = (xx.sg_dense(dim=280).sg_dense(dim=280).sg_dense(dim=70))
    # shared recognizer part
    recog_shared = shared.sg_dense(dim=128)
    # discriminator end
    disc = shared.sg_dense(dim=1, act='linear').sg_squeeze()
    # categorical recognizer end
    recog_cat = recog_shared.sg_dense(dim=num_category, act='linear')
    # continuous recognizer end
    recog_cont = recog_shared[batch_size:, :].sg_dense(dim=num_cont, act='sigmoid')

#
# loss and train ops
#

loss_disc = tf.reduce_mean(disc.sg_bce(target=y_disc))  # discriminator loss
loss_gen = tf.reduce_mean(disc.sg_reuse(input=gen).sg_bce(target=y))  # generator loss
loss_recog = tf.reduce_mean(recog_cat.sg_ce(target=label)) \
             + tf.reduce_mean(recog_cont.sg_mse(target=z_cont))  # recognizer loss

train_disc = tf.sg_optim(loss_disc + loss_recog, lr=0.0001, category='discriminator')  # discriminator train ops
train_gen = tf.sg_optim(loss_gen + loss_recog, lr=0.001, category='generator')  # generator train ops


#
# training
#

# def alternate training func
@tf.sg_train_func
def alt_train(sess, opt):
    l_disc = sess.run([loss_disc, train_disc])[0]  # training discriminator
    l_gen = sess.run([loss_gen, train_gen])[0]  # training generator
    return np.mean(l_disc) + np.mean(l_gen)
print(1)
# do training
# alt_train(log_interval=10, max_ep=30, ep_size=data.train.num_batch, early_stop=False)
#d1
alt_train(log_interval=10, max_ep=4000, ep_size=data.train.num_batch, early_stop=False)

