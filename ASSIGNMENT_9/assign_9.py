import numpy as np
import matplotlib.pyplot as plt
import random
th_prob=0.3935
lamda = 1/2 #for every 3 minutes

size = 100000

count_intx= 0
count_x_0 = 0
for i in range(size):

  #X for first three minutes
  X = np.random.poisson(lamda)
  #Y for second three minutes
  Y = np.random.poisson(lamda)

  if (X==0) and (Y!=0):
    count_intx+=1
  if (X==0):
    count_x_0 +=1
sim_prob=count_intx/count_x_0
print("Theoretical probability=%f, simulated probability=%f",(th_prob,sim_prob))

cases=['i']
x = np.arange(len(cases))
plt.bar(x + 0.00, th_prob, color = 'green', width = 0.25, label = 'Theoretical')
plt.bar(x + 1, sim_prob, color = 'indigo', width = 0.25, label = 'Simulated')
plt.xlabel('Case')
plt.ylabel('Probabilities')

plt.legend()
plt.show()
