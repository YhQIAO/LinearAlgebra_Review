import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-np.pi, np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()