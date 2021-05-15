from numpy import array
from sympy import Symbol, solve

filename = 'gauss_data.txt'
maxPivot = 0
maxIdx = 0

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
    if(abs(maxPivot) < abs(A[i][0])):
        maxPivot = A[i][0]
        maxIdx = i  # for pivoting
    B[i] = float(B[i])  # B 실수형 변환

x = [Symbol('x'+str(i)) for i in range(size)]  # size에 맞게 미지수 생성

# Command Line explanation
print("------ Ax = B 형태 가우스 소거법 ------")
print('A행렬(n*n)의 사이즈 : ', size)
print("A\n", A)
print("x\n", x)
print("B\n", B)

# pivoting
if(maxPivot != A[0][0]):
    for i in range(size):
        A[0][i], A[maxIdx][i] = A[maxIdx][i], A[0][i]
    B[0], B[maxIdx] = B[maxIdx], B[0]

# Gauss 소거법
start = 0
for k in range(1, size):
    for i in range(k, size):
        Num = A[i][start]/A[start][start]
        for j in range(size):
            A[i][j] = A[i][j]-(A[start][j]*Num)
        B[i] = B[i] - (B[start]*Num)
    start = start+1

expr = []
for i in range(size):

    this = ''
    for j in range(size):
        sign = '+'
        if(A[i][j] == 0):
            continue
        if(A[i][j] < 0):
            sign = ''
        this = this+sign+str(A[i][j])+'*'+str(x[j])
    if(B[i] > 0):
        this = this+'-'+str(B[i])
    else:
        this = this+'+'+str(B[i])
    expr.append(this)


for i in range(size):
    print(str(i+1)+'번째 방정식')
    print(expr[i])

solution = solve(expr, x)
print('연립 방정식의 해')
print(solution)
print("---------------")
