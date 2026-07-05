import numpy as np
import matplotlib.pyplot as plt

# 1. LOAD THE DATA
# names=True reads the header, delimiter=',' splits by commas
data = np.genfromtxt('py-proj/level1/gta_v_worldwide_sales_player_analytics_2013_2026.csv', delimiter=',', names=True, dtype=None, encoding='utf-8')

# 2. EXTRACT YOUR TWO NUMERIC COLUMNS
# (Replace 'Column_Name_A' with the exact header name from your CSV)
col_a = data['Column_Name_A']
col_b = data['Column_Name_B']

# 3. DO THE NUMPY MATH
# Use np.mean(), np.max(), np.min() on both columns
print(f"Column A Mean: {np.mean(col_a)}")

# 4. PLOT THE CHART
plt.scatter(col_a, col_b) # or plt.plot(), plt.bar()
plt.title("What Your Chart Is About")
plt.xlabel("Label for A")
plt.ylabel("Label for B")
plt.show()