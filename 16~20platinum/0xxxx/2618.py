import sys
input = sys.stdin.readline


n = int(input())
w = int(input())
arr =[0]
for i in range(w):
    arr.append(list(map(int,input().split())))

dp = [[1e9]*(w+1) for i in range(w+1)] #1의 마지막 사건, 2의 마지막 사건 저장
dp[0][0] = 0

dp2 = [[(0,0)]*(w+1) for i in range(w+1)]

for i in range(1,w+1):
    for j in range(i):
        if i-j!=1:
            dp[i][j] = min(dp[i][j],dp[i-1][j]+abs(arr[i][0]-arr[i-1][0])+abs(arr[i][1]-arr[i-1][1]))
            dp2[i][j] = (i-1,j)
            dp[j][i] = min(dp[j][i], dp[j][i-1] + abs(arr[i][0] - arr[i - 1][0]) + abs(arr[i][1] - arr[i - 1][1]))
            dp2[j][i] = (j,i-1)
        else:
            for k in range(j+1):
                arr[0] = [1,1]

                if dp[i][j] >dp[k][j]+abs(arr[i][0]-arr[k][0])+abs(arr[i][1]-arr[k][1]):
                    dp[i][j] = dp[k][j] + abs(arr[i][0] - arr[k][0]) + abs(arr[i][1] - arr[k][1])
                    dp2[i][j] = (k,j)

                arr[0] = [n,n]
                if dp[j][i] > dp[j][k]+abs(arr[i][0]-arr[k][0])+abs(arr[i][1]-arr[k][1]):
                    dp[j][i] = dp[j][k]+abs(arr[i][0]-arr[k][0])+abs(arr[i][1]-arr[k][1])
                    dp2[j][i] = (j,k)

mi = 1e9
for i in range(w):
    if dp[i][w]<mi:
        a = i
        b = w
        mi = dp[i][w]

    if dp[w][i]<mi:
        a = w
        b = i
        mi = dp[w][i]

print(mi)

ans = [0]*(w+1)

while(a!=0 and b!=0):
    if a>b:
        for i in range(b+1,a+1):
            ans[i] = 1
    else:
        for i in range(a+1,b+1):
            ans[i] = 2
    c,d = dp2[a][b]

    a = c
    b = d

if a>b:
    for i in range(b+1,a+1):
        ans[i] = 1
else:
    for i in range(a+1,b+1):
        ans[i] = 2

for i in ans[1:]:
    print(i)