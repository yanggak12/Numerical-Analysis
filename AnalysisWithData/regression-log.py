from numpy import array, sum, linspace, zeros, log, exp, mean
from numpy.linalg import det
import matplotlib.pyplot as plt

x = array([0, 1, 2, 4])
yo = array([2, 4, 8, 15])

it = linspace(0, 4, 9)
itl = array(it)

itln = len(itl)
yresult = zeros(itln)

y = log(yo)
n = len(x)

xsum = sum(x)
ysum = sum(y)
xmean = mean(x)
ymean = mean(y)
xysum = sum(x*y)
x2sum = sum(x**2)

A = (n*xysum - xsum*ysum)/(n*x2sum - xsum**2)
B = ymean - A*xmean
print('A = %8.4f B= %8.4f' % (A, B))
b = exp(B)
a = A
print('a = %8.4f b = %8.4f' % (a, b))

for k in range(itln):
    yresult[k] = b * exp(a*itl[k])
    print("%5f" % yresult[k])

plt.scatter(x, yo, s=100, facecolor='purple', label='Data')
plt.plot(itl, yresult, 'k')
plt.legend()
plt.xlabel('X label')
plt.ylabel('Y label')
plt.show()
