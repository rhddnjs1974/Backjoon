import sys
input = sys.stdin.readline

def w(a,b,c):
    if a<=0 or b<= 0 or c<=0:
        return 1

    if dp[a][b][c] != "x":
        return dp[a][b][c]

    if a>20 or b>20 or c>20:
        dp[a][b][c] = w(20,20,20)
        return dp[a][b][c]

    if a<b and b<c:
        dp[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c-1)
        return dp[a][b][c]

    dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]

dp = [[["x"]*51 for i in range(51)] for j in range(51)]

while(True):
    a,b,c = map(int,input().split())
    if a==b==c==-1:
        break


    print("w(%d, %d, %d) = %d"%(a,b,c,w(a,b,c)))