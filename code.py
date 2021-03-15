import numpy as np
from scipy.stats import bernoulli

sample_size = 100000

prob_A = 0.5
prob_B = 7/12
prob_not_A_or_not_B= 0.25

#finding wether A and B are independent
sample_A = bernoulli.rvs(size = sample_size , p = prob_A)
sample_B = bernoulli.rvs(size = sample_size , p = prob_B)
sample_not_A_or_not_B = bernoulli.rvs(size = sample_size , p = prob_not_A_or_not_B)

 
   
prob_AB = 1 - prob_not_A_or_not_B
print("P(AB)=",prob_AB)
if prob_AB == prob_A * prob_B :
 print(" A and B are independent")
      
else : print("A and B are dependent")