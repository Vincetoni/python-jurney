import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# PART 1: Line Plot (y = x²)
# ==========================================
print("Generating line plot...")
x1 = list(np.arange(1, 21))
y1 =  [x**2 for x in x1]

plt.plot(x1,y1)
plt.title('Y = X²')
plt.xlabel('X')
plt.ylabel('X²')
plt.show() 
print('done')


# ==========================================
# PART 2: Scatter Plot (10 Random Points)
# ==========================================
print("Generating scatter plot...")
# Hint: Generate 10 random numbers for X and 10 for Y
x2 = np.random.rand(10)
y2 = np.random.rand(10)

plt.clf()
plt.scatter(x2,y2)
plt.show()
print('done')


# ==========================================
# PART 3: 2D Array and Images
# ==========================================
print("Generating 2D pixel grid...")

grid = np.random.rand(5, 5) 

plt.imshow(grid, cmap="gray")
plt.show()
print('done')