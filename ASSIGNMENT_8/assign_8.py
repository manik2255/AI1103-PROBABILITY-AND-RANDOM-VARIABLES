import numpy as np
import matplotlib.pyplot as plt
th_prob=1/55
sample_size=10000
SampleA=[0]*sample_size
sampleB=[0]*sample_size
sampleC=[0]*sample_size
count=0
for i in range(sample_size):
    A=np.random.choice([0,1],p=[4/12,8/12])
    if A==0:
        B=np.random.choice([0,1],p=[3/11,8/11])
        if B==0:
          C=np.random.choice([0,1],p=[2/10,8/10])
          if C==0:
            count+=1
sim_prob=count/sample_size
print("Theoretical probability=%f, simulated probability=%f"%(th_prob,sim_prob))

cases=['i']

x = np.arange(len(cases))
plt.bar(x + 0.00, th_prob, color = 'green', width = 0.25, label = 'Theoretical')
plt.bar(x + 1, sim_prob, color = 'indigo', width = 0.25, label = 'Simulated')
plt.xlabel('Case')
plt.ylabel('Probabilities')

plt.legend()
plt.show()
