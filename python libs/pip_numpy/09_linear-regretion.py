import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample data
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Independent variable
y = np.array([2, 4, 5, 4, 5])  # Dependent variable

# Create and fit the model
model = LinearRegression()
model.fit(x, y)

# Predict
y_pred = model.predict(x)

# Plot
plt.scatter(x, y, color='blue', label='Data points')
plt.plot(x, y_pred, color='red', label='Regression line')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

# Coefficients
print("Slope (Coefficient):", model.coef_[0])
print("Intercept:", model.intercept_)