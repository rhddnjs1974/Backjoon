import sys
input = sys.stdin.readline

m,n,k = map(int,input().split())

limit = 10**18
ma = n+m+2
comb = [[0]*ma for i in range(ma)]

for i in range(ma):
    comb[i][0] = 1
    comb[i][i] = 1

for i in range(1,ma):
    for j in range(1,i):
        comb[i][j] = comb[i-1][j-1]+comb[i-1][j]
        if comb[i][j] > limit:
            comb[i][j] = limit

ans = []
last = 1

for pos in range(m):
    remain = m-(pos+1)
    for x in range(last,n+1):
        now = comb[(n-x+1)+remain-1][remain]
        if k > now:
            k -= now
        else:
            ans.append(x)
            last = x
            break

for i in range(m):
    print(ans[i],end=" ")