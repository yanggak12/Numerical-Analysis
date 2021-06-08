from numpy import array, sum, linspace, zeros
from numpy.linalg import det
import matplotlib.pyplot as plt

x = array([0, 1, 2])
y = array([1, 3, 2])

it = linspace(0, 2, 21)
itl = array(it)

n = len(x)
itln = len(itl)

x1sum = sum(x)
y1sum = sum(y)
x2sum = sum(x**2)
x3sum = sum(x**3)
x4sum = sum(x**4)
xysum = sum(x*y)
x2ysum = sum((x**2)*y)

yresult = zeros(itln)

eq = array([[x2sum, x3sum, x4sum],
            [x1sum, x2sum, x3sum],
            [n, x1sum, x2sum]])
rig = array([x2ysum, xysum, y1sum])

detabc = det(eq)

eqc = array([[x2ysum, x3sum, x4sum],
            [xysum, x2sum, x3sum],
            [y1sum, x1sum, x2sum]])

eqb = array([[x2sum, x2ysum, x4sum],
            [x1sum, xysum, x3sum],
            [n, y1sum, x2sum]])

eqa = array([[x2sum, x3sum, x2ysum],
            [x1sum, x2sum, xysum],
            [n, x1sum, y1sum]])

detc = det(eqc)
detb = det(eqb)
deta = det(eqa)
a = deta/detabc
b = detb/detabc
c = detc/detabc

print('a = ', a, 'b = ', b, 'c = ', c)

for k in range(itln):
    yresult[k] = a * itl[k]**2+b*itl[k]+c

plt.scatter(x, y, s=100, facecolor='purple', label='Data')
plt.plot(itl, yresult, 'k')
plt.legend()
plt.xlabel('X label')
plt.ylabel('Y label')
plt.show()
