from scipy import stats

# Sample data
group1 = np.array([23, 25, 28, 30, 27])
group2 = np.array([20, 22, 25, 24, 23])

# Perform t-test
t_stat, p_value = stats.ttest_ind(group1, group2)
print("T-statistic:", t_stat)
print("P-value:", p_value)

# Interpret p-value
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis (significant difference)")
else:
    print("Fail to reject the null hypothesis (no significant difference)")