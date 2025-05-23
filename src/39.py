import numpy as np
from scipy.optimize import minimize

def f(x):
    return x[0]**2 + 3*x[1] - 4

initial_guess = [0.5, 0.5]
result = minimize(f, initial_guess)
print(result)
