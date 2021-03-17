import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 100)
f =  np.exp(-x)
plt.title("probability density function")
plt.plot(x, f, linewidth=2, label=r"$f(x) = e^{-x}$")
plt.xlim(0, 100)
plt.ylabel("f(x)") 
plt.xlabel("x")
plt.legend(fontsize=14)
plt.show()