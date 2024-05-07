import sys
input = sys.stdin.readline

T = int(input())

dp1 = [0] * (10004)
dp2 = [0] * (10004)
dp3 = [0] * (10004)
dp1[0] = 1
dp2[0] = 0
dp3[0] = 0

for i in range(10000):
    dp1[i + 1] += dp1[i]
    dp2[i + 2] += dp1[i]
    dp3[i + 3] += dp1[i]

    dp2[i + 2] += dp2[i]
    dp3[i + 3] += dp2[i]

    dp3[i + 3] += dp3[i]

for i in range(T):
    a = int(input())
    print(dp1[a]+dp2[a]+dp3[a])


