import numpy as np

# Sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Covariance
covariance = np.cov(x, y)[0, 1]
print("Covariance:", covariance)

# Correlation (Pearson)
correlation = np.corrcoef(x, y)[0, 1]
print("Correlation:", correlation)