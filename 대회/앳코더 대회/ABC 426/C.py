import sys
input = sys.stdin.readline

n,q = map(int,input().split())

minnow = 1
dp = [0]
for i in range(1,n+1):
    dp.append(1)

for i in range(q):
    x,y = map(int,input().split())

    if x>=minnow:
        ans = 0
        for j in range(minnow,x+1):
            ans += dp[j]
        dp[y] += ans
        print(ans)
        minnow = x+1
    else:
        print(0)