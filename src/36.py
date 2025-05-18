import numpy as np
from scipy.integrate import odeint

def dS_dt(S):
    # Example of some differential equation model 
    return 1/S

t = np.linspace(0, 15, 100)  # Time points in seconds
S = odeint(dS_dt, 1.0, t)  # Solve the differential equation and get the solution at time points `t`

print(S)
