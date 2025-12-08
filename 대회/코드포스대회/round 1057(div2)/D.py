import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    A = list(map(int,input().split()))
    ans = 10**15
    
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 10**15
    dp[2] = abs(A[1]-A[0])
    for i in range(2,n):
        dp[i+1] = min(dp[i-1]+abs(A[i]-A[i-1]), dp[i-2]+max(A[i],A[i-1],A[i-2])-min((A[i],A[i-1],A[i-2])))
    ans = min(ans,dp[-1])
    
    p = A[0]
    A = A[1:]
    A.append(p)
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 10**15
    dp[2] = abs(A[1]-A[0])
    for i in range(2,n):
        dp[i+1] = min(dp[i-1]+abs(A[i]-A[i-1]), dp[i-2]+max(A[i],A[i-1],A[i-2])-min((A[i],A[i-1],A[i-2])))
    ans = min(ans,dp[-1])
    
    
    p = A[0]
    A = A[1:]
    A.append(p)
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 10**15
    dp[2] = abs(A[1]-A[0])
    for i in range(2,n):
        dp[i+1] = min(dp[i-1]+abs(A[i]-A[i-1]), dp[i-2]+max(A[i],A[i-1],A[i-2])-min((A[i],A[i-1],A[i-2])))
    ans = min(ans,dp[-1])
    
 
    print(ans)