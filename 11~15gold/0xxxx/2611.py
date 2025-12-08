import sys
input = sys.stdin.readline
from collections import deque

def topology_sort():

    result = []
    q = deque()

    q.append(1)

    while q:
        now = q.popleft()
        result.append(now)
        for i,point in graph[now]:
            indegree[i]-=1
            dp[i] = max(dp[i],dp[now] + point)
            if indegree[i]==0 and i!=1:
                q.append(i)

    return result

V = int(input())
E = int(input())
indegree= [0]*(V+1)
graph = [[] for i in range(V+1)]
rgraph = [[] for i in range(V+1)]

canarrive=[]
canarinfo=[]
dp = [0]*(V+1)

for i in range(E):
    a,b,c = map(int,input().split())
    if b==1:
        canarrive.append(a)
        canarinfo.append(c)

    graph[a].append((b,c))
    rgraph[b].append((a,c))
    indegree[b] += 1


topology_sort()


ma = 0
for i in range(len(canarrive)):
    if ma<dp[canarrive[i]]+canarinfo[i]:
        ma = dp[canarrive[i]]+canarinfo[i]
        ans = canarrive[i]


print(ma)

q = deque()
result = [1,ans]
q.append(ans)
while (q):
    i = q.popleft()
    for j,point in rgraph[i]:
        if dp[j]+point == dp[i]:
            result.append(j)
            q.append(j)

result.append(1)
result.reverse()
print(*result)

