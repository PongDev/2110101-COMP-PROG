import numpy as np

def p(X):
    return 1/(1+(np.e**(-(-3.98+(0.1*X[:,0])+(0.5*X[:,1])))))

exec(input().strip())