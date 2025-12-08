import sys
input = sys.stdin.readline

########################################
dp = [0,1]
for i in range(10000):
    dp.append(dp[i]+dp[i+1])

print(dp[int(input())])