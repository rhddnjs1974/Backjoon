import sys
input = sys.stdin.readline

def game(a,b,turn): #turn : 1 is me
    if dp[a][b]!=0:
        return dp[a][b]
    if b==0:
        if turn ==1:
            return arr[a]
        return 0
    
    if turn==1:
        playl = arr[a]+game(a+1,b-1,1-turn)
        playr = arr[a+b]+game(a,b-1,1-turn)
        dp[a][b] = max(playl,playr)
    else:
        playl = game(a+1,b-1,1-turn)
        playr = game(a,b-1,1-turn)
        dp[a][b] = min(playl,playr)
    return dp[a][b]



t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    dp = [[0]*(n) for i in range(n)] #dp[i][j] : i~i+j가 남았을때.
    
    ans = game(0,n-1,1)
    print(ans)
