n = int(input())
dp = [0]*1001
dp[1] = 1
for i in range(2,1001):
    if dp[i-1]==0:
        dp[i]=1
    if i>=4 and dp[i-4]==0:
        dp[i] = 1
    if i>=16 and dp[i-16]==0:
        dp[i] = 1
    if i>=64 and dp[i-64]==0:
        dp[i] = 1


k = n%5
if k==2 or k==0:
    print("CY")
else:
    print("SK")
