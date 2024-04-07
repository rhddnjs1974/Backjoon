import sys
input = sys.stdin.readline
LOG = 20

m = int(input())
arr = list(map(int,input().split()))

F = [[0]*(LOG) for i in range(m+1)]

for i in range(m):
    F[i+1][0] = arr[i]

for i in range(1,LOG):
    for j in range(1,m+1):
        F[j][i] = F[F[j][i-1]][i-1]

Q = int(input())
for a in range(Q):
    n, x = map(int,input().split())


    for i in range(LOG-1,-1,-1):
        if n>=2**i:
            n-=2**i
            x = F[x][i]

    print(x)