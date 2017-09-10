import numpy as np
from scipy.stats import scoreatpercentile

data=np.loadtxt("test1.csv",delimiter=',',usecols=(0,1),skiprows=2,dtype='int',unpack=True)
