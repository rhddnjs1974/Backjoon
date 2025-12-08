import sys
input = sys.stdin.readline

N,Q = map(int,input().split())
arr = list(map(int,input().split()))
prefix = [0]
for i in arr:
    prefix.append(i+prefix[-1])

c = 0
for i in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        c+= query[1]
    else:
        l = (query[1]-1+c)%N
        r = (query[2]-1+c)%N
        
        if l<=r:
            print(prefix[r+1]-prefix[l])
        else:
            print(prefix[-1]-prefix[l]+prefix[r+1])
            