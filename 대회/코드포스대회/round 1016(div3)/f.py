import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    arr = list(input().split())
    can = []
    s = set() # -1 체크용
    ma = 0
    for i in range(m):
        b = list(input().split())
        can.append([])
        for j in range(n):
            if arr[j] == b[j]:
                can[i].append(j)
                s.add(j)
        ma = max(ma,len(can[i]))
        
    if len(s)!=n:
        print(-1)
    else:
        print(3*n-2*ma)