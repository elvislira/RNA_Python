import numpy as np


entradas = np.array([-1, 7, 5])
pesos = np.array([0.8, 0.1, 0.0])

def soma(e, p):
    return e.dot(p)

def step_function(s):
    if s > 0:
        return 1
    
    return 0

s = soma(entradas, pesos)

print(step_function(s))
