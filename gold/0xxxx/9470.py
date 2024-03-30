import sys
input = sys.stdin.readline
from collections import deque

def topology_sort():
    result = []
    q = deque()

    for i in range(1,M+1):
        if indegree[i]==0:
            q.append(i)
            dp[i] = 1

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            if dp[now] not in dpdp[i]:
                dpdp[i][dp[now]] = 1
            else:
                dpdp[i][dp[now]] += 1
            indegree[i]-=1
            if indegree[i]==0:
                ma = 0
                for k in dpdp[i]:
                    if ma<k:
                        ma=k
                        nn=dpdp[i][k]
                    if nn==1:
                        dp[i] = ma
                    else:
                        dp[i] = ma+1
                q.append(i)

    return result

T = int(input())
for i in range(1,T+1):
    K,M,P = map(int,input().split())
    indegree= [0]*(M+1)
    graph = [[] for i in range(M+1)]
    dp = [0]*(M+1)
    dpdp = [0]
    for x in range(M):
        dpdp.append({})

    for j in range(P):
        a,b = map(int,input().split())
        graph[a].append(b)
        indegree[b] += 1

    topology_sort()
    print(i,dp[M])