import numpy as np
from sklearn.linear_model import LinearRegression

# Example data
x = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 4, 6, 7, 3])

model = LinearRegression().fit(x, y)
print(model.coef_, model.intercept_)
