# 두 점을 잇는 직선을 할선 이라고 한다.
# 앞서 살펴본 Newton-Raphson 방법은 수렴속도는 빠르나 초기값을 정해주어야하고 미분값 계산이 필요하여 번거로운 과정이 있었다.
# 하지만 할선법은 미분 대신 두 점을 지정하고 두점을 연결하는 할선을 이용하여 x축과의 교점을 새로운 점으로 지정하여 반복하여 근에 접근하는 방법이다.
# 흔히 알고 있는 직선 방정식을 활용하여 점화식을 구한다. 
# 직선의 방정식 : y-y1 = m(x-x1) ( => 기울기 m : y1-y0/x1-x0)
# 위 식을  f(x)-f(x1) = (f(x1)-f(x0))/(x1-x0) * (x-x1) 꼴로 나타내어 점화식을 구하면
# x2 = (x1-f(x1)) * (x1-x0) / (f(x1)-f(x0)) 로 정의할 수 있다.

# - 할선법은 두개의 점으로 과정을 시작하며 방정식에 대한 미분을 요구하지 않는다.
# - Newton-Raphson보다 수렴속도 느림
# - 이분법보다 함수 계산량 많음


from numpy import zeros, array
import matplotlib.pyplot as plt


def f(x):
    return -x**2 + 6.0*x - 5.0


n = 7
xs = zeros(n)
x0 = -2.0
x1 = 3.0
itl = range(0, 7)
it = array(itl)

for k in range(n):
    x2 = x1-f(x1) * ((x1-x0) / (f(x1)-f(x0)))
    x0 = x1
    x1 = x2
    xs[k] = x2

print("%5s %8s" % ('k', 'x'))
for k in range(n):
    print("%5d %9.4f" % (k+1, xs[k]))

plt.plot(it, xs, 'ko-')
plt.xlabel('Iteration')
plt.ylabel('x')
plt.show()
