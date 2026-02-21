import sys
import math
input = sys.stdin.readline

a = input().rstrip()
K = int(input())


arr = []
for i in a:
    if i==":":
        continue
    if i==")":
        arr.append(0)
    else:
        arr.append(1)
N = len(arr)


dp = [[[[1000]*2 for f1 in range(K+1)] for f0 in range(K+1)] for run in range(N+2)]

if arr[0]==0:
    dp[1][0][0][0] = 0
    if K!=0:
        dp[1][1][0][1] = 0
else:
    dp[1][0][0][1] = 0
    if K!=0:
        dp[1][0][1][0] = 0


calculate = [0]*(N+2)
for i in range(1, N+2):
    if i==1:
        calculate[i]=2
    elif i<10:
        calculate[i]=3
    else:
        calculate[i]=4

for i in range(1, N):
    ndp = [[[[1000]*2 for f1 in range(K+1)] for f0 in range(K+1)] for run in range(N+2)]

    for run in range(1, i+2):
        for f0 in range((K//2)+1):
            for f1 in range((K//2)+1):
                if dp[run][f0][f1][0] == 1000 and dp[run][f0][f1][1] == 1000:
                    continue
                # 0
                if arr[i]!=0:
                    if f0+f1+1<=K:
                        ndp[run+1][f0][f1+1][0] = min(ndp[run+1][f0][f1+1][0], dp[run][f0][f1][0])
                        ndp[1][f0][f1+1][0] = min(ndp[1][f0][f1+1][0], dp[run][f0][f1][1]+calculate[run])
                else:
                    if f0+f1<=K:
                        ndp[run+1][f0][f1][0] = min(ndp[run+1][f0][f1][0], dp[run][f0][f1][0])
                        ndp[1][f0][f1][0] = min(ndp[1][f0][f1][0], dp[run][f0][f1][1]+calculate[run])
                    
                # 1
                if arr[i]!=0:
                    if f0+f1<=K:
                        ndp[1][f0][f1][1] = min(ndp[1][f0][f1][1], dp[run][f0][f1][0]+calculate[run])
                        ndp[run+1][f0][f1][1] = min(ndp[run+1][f0][f1][1], dp[run][f0][f1][1])
                else:
                    if f0+f1+1<=K:
                        ndp[1][f0+1][f1][1] = min(ndp[1][f0+1][f1][1] , dp[run][f0][f1][0]+calculate[run])
                        ndp[run+1][f0+1][f1][1] = min(ndp[run+1][f0+1][f1][1], dp[run][f0][f1][1])
    
    dp = ndp

ans = 1000
for run in range(1, N+1):
    for f in range((K//2)+1):
        ans= min(ans,dp[run][f][f][0]+calculate[run])
        ans= min(ans,dp[run][f][f][1]+calculate[run])

print(ans)
