# PROMPT:
# Example code for Linear Regression in Python>

# ANSWER:
import numpy as np
import matplotlib.pyplot as plt

# Generate random data-set
np.random.seed(0)
x = np.random.rand(100, 1)
y = 2 + 3 * x + np.random.rand(100, 1)

# Plot the data-set
plt.scatter(x,y,s=10)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Building Xbar 
one = np.ones((x.shape[0],1))
Xbar = np.concatenate((one, x), axis = 1)

# Calculating weights of the fitting line 
A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w = np.dot(np.linalg.pinv(A), b)
print('w = ', w)

# Preparing the fitting line 
w_0 = w[0][0]
w_1 = w[1][0]
x0 = np.linspace(0, 1, 2, endpoint=True)
y0 = w_0 + w_1*x0

# Drawing the fitting line 
plt.plot(x0, y0, 'r', label = 'fitting line')
plt.scatter(x, y, s=10)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()