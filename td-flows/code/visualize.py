import numpy as np
import matplotlib.pyplot as plt

# Grid
x, y = np.meshgrid(np.linspace(-3, 3, 20), np.linspace(-3, 3, 20))

# Define a "flow": here, gradient of a Gaussian
mu = np.array([0, 0])
sigma = 1.0
dx = -x * np.exp(-(x**2 + y**2) / (2 * sigma**2))
dy = -y * np.exp(-(x**2 + y**2) / (2 * sigma**2))

# Plot
plt.figure(figsize=(6, 6))
plt.streamplot(x, y, dx, dy, density=1.2, color="blue")
plt.title("Probability Flow (Score Field)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
