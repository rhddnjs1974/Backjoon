import sys
input = sys.stdin.readline

T = int(input())

def primelist(n):
    arr = [0,0] + [1]*(n-1)
    
    for i in range(2,int((n)**0.5)+1):
        if arr[i]==1:
            for j in range(i*i,n+1,i):
                arr[j] = 0
    
    return arr

x = primelist(5000)
primearr = [1]
for i in range(2,5000):
    if x[i]==1:
        primearr.append(i)


for test in range(T):
    N = int(input())
    arr = [[0]*(N*N) for i in range(N*N)]
    t= 0
    for i in range(N):
        for j in range(N):
            arr[i*N+j][i+j*N] = primearr[t]
            t+=1
    
    
    now = 4
    for i in range(N*N):
        for j in range(N*N):
            if arr[i][j] == 0:
                arr[i][j] = now
            
                now+=1
                while(now<primearr[t] and x[now]!=0):
                    now+=1
    
    if N==2:
        arr[1][2] = 5
        arr[3][3] = 2
    
    for i in arr:
        print(*i)