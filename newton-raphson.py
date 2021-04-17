# Newton-Raphson 방법으로 f(x) 근을 구하려면 초기값을 예측해야한다.
# Newton-Raphson 반복 과정 원리
# 1) x0를 초기값이라고 할때, f(x0) = 0 을 만족하면 x0가 근이다.
# 2) f(x0) !=0 일때 x1 = x0+h로 두고 대입하면 f(x1) = 0 이라면 x1 이 근
# 3) f(x1) = 0이 아니라면 x2 = x1+h로 두고 위 과정 반복.
# 위 과정의 식을 테일러 급수로 나타내면 f(x1) = f(x0+h) = f(x0)+hf'(x0)+1/2!h^2f''(x0)+... = 0 이다.
# 위 식에서 O(h^2) 이상의 항을 버리면 f(x0)+hf'(x0) = 0 의 식이 나온다. 
# 위 식을 통해 x1을 추출, x2를 추출 .. 과정을 반복하는것이 Newton-Raphson 방법이다.
# 위 식을 정리하여 점화식을 찾아내면 x[k+1] = x[k] - f(x[k])/f'(x[k]) 이다. 

# - 이분법과 달리 두 점을 구간으로 잡지 않고 초기값만 가지고 시작하므로 적절한 초기값을 정하는 것이 중요하다
# - 발산하려는 경우 프로그램을 멈추고 초기값을 다르게 주어 다시 분석해야한다.

from numpy import zeros, array
import matplotlib.pyplot as plt


def f(x):
    return -x**2 + 6.0*x - 5.0


def df(x):
    return -2.0*x + 6.0


n = 7
x0 = -2.0
x = zeros(n)
x[0] = x0
itl = range(0, 7)
it = array(itl)

for k in range(n-1):
    x[k+1] = x[k]-f(x[k])/df(x[k])

print("%5s %8s" % ('k', 'x'))
for k in range(n):
    print("%4d %9.4f" % (k+1, x[k]))

plt.plot(it, x, 'ko-')
plt.xlabel('Iteration')
plt.ylabel('x')
plt.show()
