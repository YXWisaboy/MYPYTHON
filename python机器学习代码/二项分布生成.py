import numpy as np
import matplotlib.pyplot as mat
cash=np.zeros(100000)
cash[0]=1000
s=np.random.binomial(9,0.5,size=len(cash))
for i in range(1,len(cash)):
	if(s[i]<5):
		cash[i]=cash[i-1]-1
		i=i+1
	elif(s[i]<10):
		cash[i]=cash[i-1]+1
		i=i+1
	else:
		print("error")

print(s.max(),s.min())
mat.plot(np.arange(len(cash)),cash)
mat.show()
