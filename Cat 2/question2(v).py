import numpy as np
from scipy.interpolate import UnivariateSpline

# Example data
x = np.array([0, 1, 2, 3, 4])
y = np.array([2.9, 3.5, 4.8, 5.2, 9.1])

spline = UnivariateSpline(x, y)
print(spline(2.5))  # Interpolated value at x=2.5
