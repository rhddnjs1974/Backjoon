n = int(input())
dp = [-1]*11
ans=0
for i in range(n):
    a,b = map(int,input().split())
    if dp[a]==-1:
        dp[a]=b
    elif dp[a]==b:
        continue
    else:
        dp[a] =b
        ans+=1
print(ans)