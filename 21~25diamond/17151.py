import sys
input = sys.stdin.readline

n,h,alpha,beta = map(int,input().split())
dp = [100000000000000]*(n)
arr= []
for _ in range(n):
    x,y = map(int,input().split())
    arr.append((x,y))
    
slope = []
for k in range(n-1):
    slope.append( (arr[k+1][1]-arr[k][1])/(arr[k+1][0]-arr[k][0])  )
      

dp[0] = (h-arr[0][1])*alpha
for i in range(n):
    Left = [0]*(n)
    Right = [0]*(n)
    M=0
    for j in range(i,n-1):
        g = arr[j][1] + slope[j]*(arr[j][0]-arr[j][0])
        u = h-g
        s = arr[j][0] - arr[i][0]
        L = (u*u - s*s)/(2*u)
        M= max(M,L)
        
        g = arr[j][1] + slope[j]*(arr[j+1][0]-arr[j][0])
        u = h-g
        s = arr[j+1][0] - arr[i][0]
        L = (u*u - s*s)/(2*u)
        M= max(M,L)

        Left[j+1] = M
    
    M=0
    for j in range(i-1,-1,-1):
        g = arr[j][1] + slope[j]*(arr[j][0]-arr[j][0])
        u = h-g
        s = arr[i][0] - arr[j][0]
        L = (u*u - s*s)/(2*u)
        M= max(M,L)
        
        g = arr[j][1] + slope[j]*(arr[j+1][0]-arr[j][0])
        u = h-g
        s = arr[i][0] - arr[j+1][0]
        L = (u*u - s*s)/(2*u)
        M= max(M,L)
        Right[j] = M
        
    for j in range(i,n):
        r = (arr[j][0]-arr[i][0])*0.5
        need = max(Left[j],Right[j])
        if r>=need:
            cost = alpha*(h-arr[j][1]) + beta*((arr[j][0]-arr[i][0])**2)
            dp[j] = min(dp[j],dp[i]+cost)
        
if dp[-1]>=5000000000000:
    print("impossible")
else:
    print(int(dp[-1]))
    
