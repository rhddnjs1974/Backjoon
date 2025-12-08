import sys
input = sys.stdin.readline

t = int(input())

dp0 = [1,0]
dp1 = [0,1]


for i in range(40):
    dp0.append(dp0[-1]+dp0[-2])
    dp1.append(dp1[-1]+dp1[-2])

for _ in range(t):
    n = int(input())
    print(dp0[n],dp1[n])