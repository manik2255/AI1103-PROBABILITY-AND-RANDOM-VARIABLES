import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon
import seaborn as sns
sns.set(color_codes=True)
sns.set(rc={'figure.figsize':(6,6)})

x = np.linspace(0, 100, 101)
f =  np.exp(-x)
plt.plot(x, f, linewidth=2, label=r"$f(x) = e^{-x}$")
plt.xlim(0, 100)
plt.ylabel("f(x)") 
plt.xlabel("x")
plt.legend(fontsize=14)
plt.show()



data_expon = expon.rvs(scale=1,loc=0,size=1000)
plt.title("probability density function")
ax = sns.distplot(data_expon,
                  kde=True,
                  bins=100,
                  color='blue',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Exponential Distribution', ylabel='Frequency')
