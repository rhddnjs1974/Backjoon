from collections import deque

N,K = map(int,input().split())
A = list(map(int,input().split()))
move = []
for i in range(1,K+1):
    bnum,*B = map(int,input().split())
    
    now = [0]*N
    for x in B:
        now[x-1]+=(i%5)
    
    move.append(now)


visit = {}
visit[tuple(A)] = 0
q = deque([tuple(A)])

while q:
    arr = q.popleft()
    for arr22 in move:
        arr2 = arr22[:]
        for i in range(N):
            arr2[i] = (arr[i]+arr2[i])%5

        if tuple(arr2) in visit:
            if visit[tuple(arr2)] <= visit[tuple(arr)]+1:
                continue
            
        visit[tuple(arr2)] = visit[tuple(arr)]+1

        q.append(tuple(arr2))


a = tuple([0]*N)
b = tuple([1]*N)
c = tuple([2]*N)
d = tuple([3]*N)
e = tuple([4]*N)


ans = 1e15
if a in visit:
    ans = min(ans,visit[a])
if b in visit:
    ans = min(ans,visit[b])
if c in visit:
    ans = min(ans,visit[c])
if d in visit:
    ans = min(ans,visit[d])
if e in visit:
    ans = min(ans,visit[e])
    
if ans==1e15:
    print(-1)
else:
    print(ans)