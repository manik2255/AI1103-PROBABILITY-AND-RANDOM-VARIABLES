import numpy as np

n=float(input("n:\n"))
p=float(input("p:\n"))

lambd = float(n*p)

simlen = int(1e5)
binom_rv = np.random.binomial(n = n, p = p, size = simlen)
poisson_rv = np.random.poisson(lam = lambd, size = simlen)

if(np.var(binom_rv)==np.var(poisson_rv)):
    print("var(X)=Var(Y)")
elif(np.var(binom_rv)<np.var(poisson_rv)):
    print("var(X)<Var(Y)")
elif(np.var(binom_rv)>np.var(poisson_rv)):
    print("var(X)>Var(Y)")
else: 
    print("Var(X) may be larger or smaller than Var(Y) depending on the values of n,p and lambda")