entradas = [-1, 7, 5]
pesos = [0.8, 0.1, 0.0]

def soma(e, p):
    s = 0

    for i in range(len(entradas)):
        s += e[i] * p[i]
    
    return s

def step_function(s):
    if s > 0:
        return 1
    
    return 0

s = soma(entradas, pesos)

print(step_function(s))
