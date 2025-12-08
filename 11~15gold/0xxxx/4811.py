dp = [[0]*31 for i in range(31)]
for h in range(31):
    for w in range(h+1,31):
        if h==0:
            dp[w][h]=1
        else:
            dp[w][h] = dp[w-1][h] + dp[w][h-1]

while(True):
    a = int(input())
    if a==0:
        break
    print(sum(dp[a]))