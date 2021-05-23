from numpy import mean, median, var, std, array
import pandas as pd

x = array([20, 23, 25, 22, 21, 19, 18])

m = mean(x)
M = median(x)
V = var(x)
S = std(x)
print("### 시간대별 온도 변화 ###")
col = [1, 2, 3, 4, 5, 6, 7]  # Time
row = ['temp']
con = [x]
df = pd.DataFrame(con, columns=col, index=row)
print(df)
print("\n### 평균, 분산, 표준편차 ###")
col = ['평균(Mean)', '중앙값(Median)', '분산(Variance)', '표준편차(Standard deviation)']
row = ['결과']
con = [[m, M, V, S]]
df = pd.DataFrame(con, columns=col, index=row)
print(df)
