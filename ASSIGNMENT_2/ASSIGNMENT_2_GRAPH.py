import numpy as np
# import uniform distribution
from scipy.stats import uniform
from matplotlib import pyplot as plt
# data to be plotted 
x = np.arange(0,2)  
y =np.exp(-x)


def ecdf(a):
    x, counts = np.unique(a, return_counts=True)
    cusum = np.cumsum(counts)
    return x, cusum / cusum[-1]
    return x

U = uniform.rvs(size=1000)
V =-np.log(U)
x = ecdf(V)[0]
y = ecdf(V)[1]
x = np.insert(x, 0, x[0])
y = np.insert(y, 0, 0.)
plt.plot(x, y,'o',label='cdf')
plt.grid(True)
v=np.linspace(0,15,1000)
plt.plot(v,np.exp(-v),label='pdf')
plt.xlabel("$x$")
plt.ylabel("$F_x(x)$")
plt.legend(loc='best')

count=0
for i in range(1000):
  
  if x[i]<1.0:
        count +=1

print("simulated probability P(X>1) is : ",1-(count/1000))
print("Which is nearly equal to Theoritical probability P(X>1) 0.368 ")
