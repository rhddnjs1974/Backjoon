import sys
input = sys.stdin.readline

n,m = map(int,input().split())

dp = [n-1]*(n+1)

for i in range(m):
    a,b = map(int,input().split())
    dp[a]-=1
    dp[b]-=1

for i in range(1,n+1):
    x = dp[i]
    print((x*(x-1)*(x-2))//6,end=" ")