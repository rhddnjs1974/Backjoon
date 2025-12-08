import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
f = 0
for i in arr:
    if i==0:
        f+=1
if f!=0:
    print(n-f)
    exit()

prev = {}
prev[arr[0]] = 1
L = 10000000
for i in range(1,n):
    cur = {}
    cur[arr[i]]=1
    for a in prev:
        n_v = arr[i]&a
        if n_v in cur:
            cur[n_v] = min(cur[n_v],prev[a]+1)
        else:
            cur[n_v] = prev[a]+1
    if 0 in cur:
        L = min(L,cur[0])

    prev = cur

if L==10000000:
    print(-1)
else:
    print(n+L-2)