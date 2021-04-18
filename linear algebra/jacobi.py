# 선형 연립 방정식의 해를 찾을때 초기값을 가정하여 반복하는 과정을 수행하여 해를 구하는 방법을 반복법이라고 한다.
# -> 한번에 해를 찾을 가능성이 거의 없기 때문에 원하는 정확도의 해를 구하기 까지 같은 과정을 반복한다.
# * Jacobi 방법
# 미지수가 x1, x2로 두개인 연립방정식이 있다고 가정하자 
# (e.g. 2*x1-x2 = 3 |
#          5*x1+7*x2=1 )
# 1) 방정식을 미지수에 대해 정리
# 2) x1, x2는 미지수이므로 처음에는 값을 예측하여 결정 (여기서는 0 으로 함)
# 3) 초기값 x1(1) = 1/2*(3+x2(1)) | x2 = 1/7(1-5*x1(0))
# 4) 예측값 0을 미지수에 대입하여 정리한다.
# 5) 위 과정을 반복하여 근사값을 구한다.

# - 코딩을 위해 점화식 구하기
# - 미지수 xi에 대해서 정리하면 행렬의 대각성분으로 나눗셈을 한 형태가 나온다.
# -> xi(k+1) = 1/aii(bi - Σaijxij(k)) , i=1,2,...,n
# 1) 연산 시작 시 x(0)을 미리 정해줄것
# 2) 오차범위(값) 정해줄 것
# 3) 반복횟수는 고정값 혹은 2)을 활용하여 계산.


from numpy import zeros
import matplotlib.pyplot as plt

m = 10
x1j = zeros(m)
x2j = zeros(m)
x3j = zeros(m)
it = range(m)

print("%7s %9s %9s %9s" % ('k', 'x1', 'x2', 'x3'))
print("%7d %9.5f %9.5f %9.5f" % (0, x1j[0], x2j[0], x3j[0]))  # x0 예측값 0으로 가정

for k in range(m-1):
    x1j[k+1] = (-1.0+2.0*x2j[k]-3.0*x3j[k])/5.0
    x2j[k+1] = (2.0+3.0*x1j[k]-x3j[k])/9.0
    x3j[k+1] = (-3.0+2.0*x1j[k]-x2j[k])/7.0
    print("%7d %9.5f %9.5f %9.5f" % (k+1, x1j[k+1], x2j[k+1], x3j[k+1]))

plt.plot(it, x1j, 'r*-', label='x1')
plt.plot(it, x2j, 'b*-', label='x2')
plt.plot(it, x3j, 'k*-', label='x3')
plt.legend()
plt.xlabel('iteration')
plt.xlabel('Approxiimate Soultions')
plt.show()
