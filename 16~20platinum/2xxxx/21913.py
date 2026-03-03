import sys
input = sys.stdin.readline
MOD = 1000000007

n = int(input())

if n==1 or n==2:
    print(n)
    exit()
if n==3:
    print(6)
    exit()

dp = [0]*(n+3)
dp[n] = 1

for i in range(n-1,3,-1):
    s = 1
    for j in range(i-1,n+1,i-1):
        if j>i:
            s += dp[j]
        if j+1<=n and j+1>i:
            s += dp[j+1]
        if j+2<=n and j+2>i:
            s += dp[j+2]
    dp[i] = s%MOD

sum4 = 0
for k in range(4,n+1):
    sum4 += dp[k]
    sum4 %= MOD

dp3 = sum4+1
dp3 %= MOD

dp2 = sum4+dp3+1
dp2 %= MOD

print((dp2 * n)%MOD)