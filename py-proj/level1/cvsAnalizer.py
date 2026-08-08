import numpy as np
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, 'gta_v_worldwide_sales_player_analytics_2013_2026.csv')

data = np.genfromtxt(CSV_PATH, delimiter=',', skip_header=1, usecols=(11, 12), invalid_raise=False)

units_sold    = data[:, 0]
gross_revenue = data[:, 1]

print(f"Units Sold    — mean: {units_sold.mean():.0f}, max: {units_sold.max():.0f}, min: {units_sold.min():.0f}")
print(f"Gross Revenue — mean: ${gross_revenue.mean():.2f}, max: ${gross_revenue.max():.2f}, min: ${gross_revenue.min():.2f}")

plt.scatter(units_sold, gross_revenue, alpha=0.3, s=10)
plt.title("Units Sold vs Gross Revenue — GTA V (2013–2026)")
plt.xlabel("Units Sold")
plt.ylabel("Gross Revenue (USD)")
plt.show()