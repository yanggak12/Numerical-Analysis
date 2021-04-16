# 1. 주어진 구간 a<x<b 에서 중간점 c를 구한다. (c = (a+b)/2)
# 2. 중간점의 함수값을 f(c)라고 하자.
# 3. f(c)의 부호를 f(a) 또는 f(b)와 비교한다.
# 4. 부호가 다른 구간에 해가 있으므로 새로운 구간을 정의한다. (f(a) = f(c) 또는 f(b) = f(c) )
# 5. 위 과정을 반복하며 가장 근사한 해를 구한다.
# ** 구간이 적절하다면 거의 확정적으로 해를 찾을 수 있다.
# ** 하지만 모든 영역을 나누어 가면서 탐색해야 하므로 시간이 오래 걸릴 수 있다.

from numpy import array, zeros, sign
import matplotlib.pyplot as plt


def f(x):
    return -x**2 + 6.0*x - 5.0


a = -2.0
b = 3.0
n = 10
c = zeros(n)
x = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

for i in range(n):
    c[i] = (a+b)/2.0
    if(sign(f(c[i])) == sign(f(a))):
        a = c[i]
    else:
        b = c[i]

print("%5s %8s" % ('k', 'c'))
for k in range(n):
    print("%5d %9.4f" % (k+1, c[k]))

plt.plot(x, c, 'ko-')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
