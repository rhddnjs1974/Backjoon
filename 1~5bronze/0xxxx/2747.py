dp = [0,1,1]

for i in range(44):
    dp.append(dp[i+1]+dp[i+2])

print(dp[int(input())])