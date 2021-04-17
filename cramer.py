# Ax = b 형태의 선형 연립 방정식을 푸는 방식
# b 행렬을 A1에서는 1열에 넣어 det(A1)을 만들고 A2에서는 2열에 넣어 det(A2)를 만든다.
# 이를 이용해 x1, x2를 구한다.
# x1 = det(A1)/det(A) , x2 = det(A2)/det(A)

from numpy import array
from numpy.linalg import det

A = array([[4, 1, -1], [3, -1, 2], [-1, 2, 3]])
B = array([-2, 1, 1])
A1 = array([[-2, 1, -1], [1, -1, 2], [1, 2, 3]])
A2 = array([[4, -2, -1], [3, 1, 2], [-1, 1, 3]])
A3 = array([[4, 1, -2], [3, -1, 1], [-1, 2, 1]])

detA = det(A)
detA1 = det(A1)
detA2 = det(A2)
detA3 = det(A3)

print('|A| = ', detA, '|A1| = ', detA1, '|A2| = ', detA2, '|A3| = ', detA3)

x1 = detA1/detA
x2 = detA2/detA
x3 = detA3/detA

print('x1 = ', x1, 'x2 = ', x2, 'x3 = ', x3)
