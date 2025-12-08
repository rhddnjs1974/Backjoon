import sys
input = sys.stdin.readline
LOG = 30

n,k,m = map(int,input().split())
arr = list(map(int,input().split()))
arr2 = list(map(int,input().split()))


F = [[0]*(LOG) for i in range(k+1)]

for i in range(k):
    F[i+1][0] = arr2[i]

for i in range(1,LOG):
    for j in range(1,k+1):
        F[j][i] = F[F[j][i-1]][i-1]


for x in arr:
    n = m-1
    for i in range(LOG-1,-1,-1):
        if n>=2**i:
            n-=2**i
            x = F[x][i]

    print(x,end=" ")