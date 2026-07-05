import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# PART 3: 2D Array and Images
# ==========================================
print("Generating 2D pixel grid...")

grid = np.random.rand(100,100) 

print(grid)
plt.imshow(grid, cmap="gray")
plt.show()
print('done')