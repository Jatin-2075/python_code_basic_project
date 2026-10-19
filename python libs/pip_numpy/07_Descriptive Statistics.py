import numpy as np
from scipy import stats

# Sample data
data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Descriptive Statistics
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Mode:", stats.mode(data)[0])  # Mode may not be unique
print("Variance:", np.var(data))
print("Standard Deviation:", np.std(data))
print("Min:", np.min(data))
print("Max:", np.max(data))
print("25th Percentile:", np.percentile(data, 25))
print("75th Percentile:", np.percentile(data, 75))