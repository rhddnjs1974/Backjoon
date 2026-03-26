N, L, I = map(int,input().split())

dp = [[0]*(L+1) for i in range(N)]

dp[0][0] = 1
dp[0][1] = 1

for i in range(1,N):
    dp[i][0] = 1
    for j in range(1,L+1):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

ans = []

L+=1
while(True):
    if I==1:
        break
    if I==2:
        ans.append(0)
        break
    now = 0

    for i in range(N):
        if sum(dp[i][:L])>=I:
            break
        now = sum(dp[i][:L])


    ans.append(i)
    I -= now
    L -= 1
    

ansarr = [0]*N
for i in ans:
    ansarr[i] = 1

ansarr.reverse()
print(*ansarr,sep="")