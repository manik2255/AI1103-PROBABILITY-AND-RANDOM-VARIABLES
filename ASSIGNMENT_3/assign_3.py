from scipy.stats import geom
import numpy as np
import matplotlib.pyplot as plt

X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p = 0.5

# Calculate geometric probability distribution
geom_pd = geom.pmf(X, p)
# Calculate cdf
geom_cd = geom.cdf(X, p)

fig, ax = plt.subplots(1, 1, figsize=(8, 8))
ax.plot(X, geom_pd, label='geom pmf')
plt.ylabel("P(x)", fontsize="10")
plt.xlabel("X", fontsize="10")
ax.vlines(X, 0, geom_pd, colors='b', lw=5, alpha=0.5)
plt.show()

fig, ax = plt.subplots(1, 1, figsize=(8, 8))
ax.plot(X, geom_pd, label='geom pmf')
plt.ylabel("P(y)", fontsize="10")
plt.xlabel("Y", fontsize="10")
ax.vlines(X, 0, geom_pd, colors='b', lw=5, alpha=0.5)
plt.show()

fig, ax = plt.subplots(1, 1, figsize=(8, 8))
ax.plot(X, geom_cd, label='geom cdf')
plt.ylabel("F_Y(y)", fontsize="10")
plt.xlabel("Y", fontsize="10")
ax.vlines(X, 0, geom_cd, colors='b', lw=5, alpha=0.5)
plt.show()
count = 0
for i in range(10000):
  X = geom.rvs(0.5)
  Y = geom.rvs(0.5)
  if 2*Y <= X:
        count += 1
        
print("Experimental probability = ", count / 10000)
print("which is approximately equal to 0.2857(theoritical probability)")
