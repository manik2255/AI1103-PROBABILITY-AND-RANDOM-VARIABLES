import numpy as np
from scipy.stats import bernoulli

sample_size = 100000

prob_B = 3/4
prob_A_or_not_B= 1/2


sample_B = bernoulli.rvs(size = sample_size , p = prob_B)
sample_A_or_not_B = bernoulli.rvs(size = sample_size , p = prob_A_or_not_B)

not_B=0
B=0
A_or_not_B=0

for i in range(sample_size):
  if sample_B[i]==0:
    not_B+=1
  elif sample_B[i]==1:
    B+=1

for i in range(sample_size):
  if sample_A_or_not_B[i]==1:
    A_or_not_B+=1

calc_prob_B=B/sample_size
calc_prob_not_B=not_B/sample_size
calc_prob_A_or_not_B=A_or_not_B/sample_size

print("calc_prob_not_B:",calc_prob_not_B )
prob_A  = (calc_prob_A_or_not_B - calc_prob_not_B)/calc_prob_B
print("prob_A:",prob_A )
print("approximately equal to theoretical value(0.333)")