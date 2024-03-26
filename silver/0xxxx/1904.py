n = int(input())

dp = [1,1]

for i in range(1000000):
    dp.append((dp[i]+dp[i+1])%15746)

print(dp[n])