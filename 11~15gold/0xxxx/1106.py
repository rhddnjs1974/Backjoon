import sys
input = sys.stdin.readline

c,n = map(int,input().split()) #c<=1000 n<=20
dp = [1e9]*2001 #i명을 만들기 위한 최소가격
dp[0] = 0
for i in range(n):
    cost, man = map(int,input().split())
    for j in range(0,2001):
        if j+man>2000:
            break
        dp[j+man] = min(dp[j+man],dp[j]+cost)

print(min(dp[c:2001]))

