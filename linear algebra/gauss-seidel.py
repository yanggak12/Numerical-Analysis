# Ax = b 꼴의 방정식에서 A를 D+U+L로 쪼개어 계산하는 방식에는 Jacobi와 Gauss-Seidel 방법 2가지가 있다.
# Gauss-Seidel 방식은 좌변에 (D+L)*x 를 두고 우변에 b-U*x 를 두어 계산하는 방식이다.
# 즉, (D+L)x[k+1] = b-x[k] 로 정리할 수 있고 점화식도 뽑아낼 수 있다. 전체적으로 Jacobi와 비슷하나 
# x2와 x3 전개 과정에 즉 D와 L이 연관된 x 는 x[k+1]차 항인 것을 알 수 있다.

from numpy import zeros
import matplotlib.pyplot as plt

m = 10
x1 = zeros(m)
x2 = zeros(m)
x3 = zeros(m)
it = range(m)

print("%7s %9s %9s %9s" % ('k', 'x1', 'x2', 'x3'))
print("%7d %9.5f %9.5f %9.5f" % (0, x1[0], x2[0], x3[0]))  # x0 예측값 0으로 가정

for k in range(m-1):
    x1[k+1] = (-1.0+2.0*x2[k]-3.0*x3[k])/5.0
    x2[k+1] = (2.0+3.0*x1[k+1]-x3[k])/9.0
    x3[k+1] = (-3.0+2.0*x1[k+1]-x2[k+1])/7.0
    print("%7d %9.5f %9.5f %9.5f" % (k+1, x1[k+1], x2[k+1], x3[k+1]))

plt.plot(it, x1, 'r*-', label='x1')
plt.plot(it, x2, 'b*-', label='x2')
plt.plot(it, x3, 'k*-', label='x3')
plt.legend()
plt.xlabel('iteration')
plt.ylabel('Approxiimate Soultions')
plt.show()
