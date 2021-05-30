from numpy import array, mean, sum
import matplotlib.pyplot as plt

x = array([1, 2, 3, 4, 5])
y = array([-8, 2, 10, 11, 20])

n = len(x)
xsum = sum(x)
ysum = sum(y)
xmean = mean(x)
ymean = mean(y)
xysum = 0
x2sum = 0

for i in range(n):
    xysum = xysum + x[i]*y[i]
    x2sum = x2sum+x[i]*x[i]

a = (n*xysum-xsum*ysum) / (n*x2sum-xsum**2)
b = ymean - a*xmean


def f(x):
    return a*x+b


print('a = ', a, 'b = ', b)
print('y = ', a, 'x +', b)

plt.scatter(x, y, s=50, facecolor='red', label='Data')
plt.plot(x, f(x), 'p--', label='Regression')
plt.legend()
plt.xlabel('X label')
plt.ylabel('Y label')
plt.show()
