# import uniform distribution
from scipy.stats import uniform
from matplotlib import pyplot as plt
import numpy as np

def ecdf(a):
    x, counts = np.unique(a, return_counts=True)
    cusum = np.cumsum(counts)
    return x, cusum / cusum[-1]
    return x

U = uniform.rvs(size=int(1e5))
V =-np.log(1-U)
x = ecdf(V)[0]
y = ecdf(V)[1]
x = np.insert(x, 0, x[0])
y = np.insert(y, 0, 0.)

plt.plot(x, y,'o',label='cdf')
plt.grid(True)
v=np.linspace(0,15,int(1e5))
plt.plot(v,np.exp(-v),label='pdf')
plt.xlabel("$x$")
plt.ylabel("$F_x(x)$")
plt.show()

x = np.random.exponential(scale=1.0, size=int(1e5))
y = np.random.exponential(scale = 1.0, size = int(1e5))
def max(x,y) :
    result = x if x>y else y
    return result

count=0
for i in range(int(1e5)):
  
  if max(x[i],y[i])<2.0 :
        count +=1
print("simulated probability P(max(X,Y)<2) is : ",(count/int(1e5)))
print("aproximately equal to theoretical value(0.748)")
