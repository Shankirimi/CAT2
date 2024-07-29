import numpy as np
from scipy.optimize import curve_fit

# Example data
x = np.array([0, 1, 2, 3, 4])
y = np.array([2.5, 3.5, 4.8, 5.2, 9.1])

def model(x, a, b):
    return a * x + b

params, _ = curve_fit(model, x, y)
print(params)
