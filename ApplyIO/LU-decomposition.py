from numpy import array, zeros, dot
import copy
from sympy import Symbol, solve


def lu(matrix, dim):  # LU분해
    L = zeros((dim, dim))
    while (matrix[0][0] == 0):
        temp = copy.deepcopy(matrix[0])
        matrix[0] = copy.deepcopy(matrix[1])
        matrix[1] = copy.deepcopy(temp)
    U = copy.deepcopy(matrix)

    for i in range(dim):
        p = copy.deepcopy(U[i][i])
        if (p == 0):
            pass
        else:
            L[i][i] = p
            U[i] /= p
            for j in range(i+1, dim):
                sum = copy.deepcopy(U[j][i])
                L[j][i] = sum
                U[j] -= copy.deepcopy(sum*U[i])
    return L, U


filename = 'gauss_data.txt'

with open(filename) as file:
    size = int(file.readline())  # 행렬의 사이즈 (size*size를 받아옴 : 입력파일의 첫째줄)
    A = [file.readline().split(' ') for _ in range(size)]
    B = file.readline().split(' ')

for i in range(size):
    A[i][2] = A[i][2].strip()  # 개행 문자 제거
B[2] = B[2].strip()

for i in range(size):
    for j in range(size):
        A[i][j] = float(A[i][j])  # 실수형으로 변환
    B[i] = float(B[i])  # B 실수형 변환

x = [Symbol('x'+str(i)) for i in range(size)]  # size에 맞게 x 생성
y = [Symbol('y'+str(i)) for i in range(size)]  # size에 맞게 y 생성

# Command Line explanation
print("------ Ax = B 형태 LU 분해법 ------")
print('A행렬(n*n)의 사이즈 : ', size)
print("A\n", array(A))
print("x\n", x)
print("B\n", B)

L, U = lu(array(A), size)  # LU 분해

print("L\n", L)
print("U\n", U)

print("# 연산에 사용할 y\n", y)

# LUx = B -> Ly = B
expr = []
for i in range(size):
    this = ''
    for j in range(size):
        sign = '+'
        if(L[i][j] == 0):
            continue
        if(L[i][j] < 0):
            sign = ''
        this = this+sign+str(L[i][j])+'*'+str(y[j])
    if(B[i] > 0):
        this = this+'-'+str(B[i])
    else:
        this = this+'+'+str(B[i])
    expr.append(this)
solY = solve(expr, y)

print("# LUx = B 형태에서 Ly = B 형태로 계산하기")
print("Ly = B\n", expr)
print("y\n", solY)

# Ux = y를 통해 x 구하기
expr2 = []
for i in range(size):
    this = ''
    for j in range(size):
        sign = '+'
        if(U[i][j] == 0):
            continue
        if(U[i][j] < 0):
            sign = ''
        this = this+sign+str(U[i][j])+'*'+str(x[j])
    if(solY[y[i]] > 0):
        this = this+'-'+str(solY[y[i]])
    else:
        this = this+'+'+str(solY[y[i]])
    expr2.append(this)
solX = solve(expr2, x)

print("# Ly = B 형태, 위에서 구한 y값으로 Ux = y 계산하기")
print("Ux = y\n", expr2)
print("x\n", solX)
