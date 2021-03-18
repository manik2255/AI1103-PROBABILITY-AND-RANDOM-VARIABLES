#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import scipy 
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 101)
f =  np.exp(-x)
plt.plot(x, f, linewidth=1, label=r"$f(x) = e^{-x}$")
plt.xlim(0, 100)
plt.ylabel("f(x)") 
plt.xlabel("x")
plt.legend(fontsize=14)
plt.show()

maxrange=50
maxlim=100.0
x = np.linspace(0,maxlim,maxrange)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list

#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
randvar = np.loadtxt('gau.dat',dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list

def gauss_pdf(x):
	return (-1)*np.exp(-x)
	
vec_gauss_pdf = scipy.vectorize(gauss_pdf)

plt.plot(x[0:(maxrange-1)].T,pdf,'o')
plt.plot(x,vec_gauss_pdf(x))#plotting the CDF
plt.grid() #creating the grid
plt.title("probability density function")
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend(["Numerical","Theory"])
