import sys
input = sys.stdin.readline

n = int(input())
a = []
for _ in range(n):
    a.append(list(map(float, input().split())))

for i in range(n):
    p = i
    for r in range(i, n):
        if a[r][i] != 0:
            p = r
            break
    
    a[i], a[p] = a[p], a[i]
    d = a[i][i]
    
    for j in range(i, n+1):
        a[i][j] /= d
        
    for r in range(n):
        if r == i:
            continue
        
        d = a[r][i]
        if d == 0:
            continue
        
        for j in range(i, n+1):
            a[r][j] -= a[i][j] * d

for i in range(n):
    print(int(round(a[i][n])), end=' ')