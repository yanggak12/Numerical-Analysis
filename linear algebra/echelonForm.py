# 사다리꼴 모양의 행렬로 바꾼다. => echelon
# Pivoting => 기본행 연산을 가장 효율적으로 활용하기 위해 연립 방정식의 순서를 바꾼다.
# 가능한 가장 위의 행의 첫번째 계수를 가장 크게 한다.

# - 방정식 해가 존재해야 할 것
# - 행렬의 대각선 성분(Pivot)이 0 이 아닐것

from numpy import array, matrix
from numpy.linalg import det
import copy

filename = 'elementary_data.txt'
with open(filename) as file:
    size = int(file.readline())  # 행렬의 사이즈 (size*size를 받아옴 : 입력파일의 첫째줄)
    matrix = [file.readline().split(' ') for _ in range(size)]

for i in range(size):
    matrix[i][size-1] = matrix[i][size-1].strip()  # 개행 문자 제거

for i in range(size):
    for j in range(size):
        matrix[i][j] = float(matrix[i][j])  # 실수형으로 변환
# pivoting
if(matrix[0][0] > matrix[1][0]):
    if(matrix[1][0] < matrix[2][0]):
        for i in range(0, 3):
            matrix[1][i], matrix[2][i] = matrix[2][i], matrix[1][i]
else:
    if(matrix[1][0] > matrix[2][0]):
        for i in range(0, 3):
            matrix[0][i], matrix[1][i] = matrix[1][i], matrix[0][i]
    else:
        for i in range(0, 3):
            matrix[0][i], matrix[2][i] = matrix[2][i], matrix[0][i]

print(matrix)
Num = matrix[1][0]/matrix[0][0]
for i in range(0, 3):
    matrix[1][i] = matrix[1][i]-(matrix[0][i]*Num)
Num = matrix[2][0]/matrix[0][0]
for i in range(0, 3):
    matrix[2][i] = matrix[2][i]-(matrix[0][i]*Num)
Num = matrix[2][1]/matrix[1][1]
for i in range(0, 3):
    matrix[2][i] = matrix[2][i]-(matrix[1][i]*Num)
print(matrix)
