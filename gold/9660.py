n = int(input())
dp = [0]*1001
dp[1] = 1
dp[2] = 0
dp[3] = 1
for i in range(4,1001):
    if dp[i-1]==0 or dp[i-3]==0 or dp[i-4]==0:
        dp[i]=1
    else:
        dp[i]=0


k = n%7
if k==2 or k==0:
    print("CY")
else:
    print("SK")