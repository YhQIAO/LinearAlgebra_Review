'''
introduction:
equation:
2x-y=0;
-x+2y=3
'''
import numpy as np
from matplotlib import pyplot as plt

x1 = np.linspace(-2, 3)
x2 = np.linspace(-2, 3)
y1 = x1 * 2
y2 = (x2 + 3) / 2.0
plt.subplot(1, 2, 1)
ax1 = plt.subplot(1, 2, 1)
ax1.grid()
ax1.set_xlim([-2, 3])
ax1.set_ylim([-2, 3])
ax1.set_aspect(1)
plt.title("Row Picture")
plt.plot(x1, y1, 'b')
plt.plot(x2, y2, 'r')

'''
x[-2  +  y[-1  = [0
   1]       2]    3]
'''
v = np.array([[2, -1], [-1, 2]])
plt.subplot(1, 2, 2)
ax2 = plt.subplot(1, 2, 2)
ax2.grid()
ax2.set_xlim([-2, 3])
ax2.set_ylim([-2, 3])
ax2.set_aspect(1)
plt.title("Col Picture")
plt.quiver(0, 0, v[0, 0], v[0, 1], color='b', scale=5)
plt.quiver(0, 0, v[1, 0], v[1, 1], color='r', scale=5)
plt.quiver(0, 0, 0, 3, color='g', scale=5)
plt.show()

'''
2x- y     = 0
-x+2y-z   =-1
  -3y+4z  = 4
'''
A=np.array([[2,-1,0],
            [-1,2,-1],
            [0,-3,4]])
b = np.array([[0],[-1],[4]])
x = np.matmul(np.linalg.inv(A), b)
print(x)
