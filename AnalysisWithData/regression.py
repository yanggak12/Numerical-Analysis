from numpy import array
import matplotlib.pyplot as plt

x = array([0, 1, 2])
y = array([1, 3, 2])


def f(x):
    return 1/2*x+3/2


plt.scatter(x, y, s=100, facecolor='purple', label='Data')
plt.plot(x, f(x), 'p--', label='Regression')
plt.legend()
plt.xlabel('X label')
plt.ylabel('Y label')
plt.show()
