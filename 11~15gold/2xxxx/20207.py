N = int(input())
arr = [[0]*N for i in range(365)]

d = []
for i in range(N):
    S,E = map(int,input().split())
    d.append((S,-E))

d.sort()
for s,e in d:
    e = -e
    i = 0
    while(arr[s-1][i]==1):
        i+=1
    
    for x in range(s-1,e):
        arr[x][i] = 1



dp = [0]*366
for i in range(365):
    for j in range(N):
        if arr[i][j]==1:
            dp[i] = j+1


ans = 0

now = 0
nowmax = 0

for i in range(366):
    if dp[i]==0 and now>0:
        ans += (now*nowmax)
        now = 0
        nowmax = 0
        continue
    
    if dp[i]!=0:
        now += 1
        nowmax = max(nowmax,dp[i])
        
print(ans)