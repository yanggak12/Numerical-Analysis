# 연속함수 g(x)에 대해서 g(x) = x 를 만족하는 해를 고정점(fixed point)라고 할때
# 1. f(x) = 0의 해 A를 구하는 문제
# - 함수 g(x) = x - f(x) 로 정의하면 g(A) = A 가 되므로 g(x)의 고정점을 찾는 문제이다.
# 2. f(x) = g(x) - x 로 정의 했을때 f(x) = 0 의 해를 구하는 문제

# => f(x) = 0 과 g(x) = x 해를 찾는 문제들은 서로 동치다.
# 적절한 반복함수 g(x)를 정의하면 고정점 반복법을 이용하여 f(x) = 0의 근사해를 구할 수 있다.

# - 그래프가 있을때 y=x그래프를 활용하여 y값의 위치를 통해 x값의 위치를 구하여 계산할 수 있다.
# - f(x) = -x^2 + 6x -5 가 있으면 좌변에 1차의 x가 오도록 수정
# 6x = x^2 + 5
# x = 1/6(x^2 + 5)
# => x = g(x) 꼴의 형태

from numpy import zeros, array
import matplotlib.pyplot as plt


def g(x):
    return 1.0/6.0*(x**2+5)


n = 15
x0 = 3.0
x = zeros(n)
x[0] = x0
itl = range(1, 16)
it = array(itl)

for i in range(n-1):
    x[i+1] = g(x[i])

print("%5s %8s" % ('k', 'x'))
for k in range(n):
    print("%4d %9.4f" % (k+1, x[k]))

plt.plot(it, x, 'ko--')
plt.xlabel('Iteration')
plt.ylabel('x')
plt.show()
