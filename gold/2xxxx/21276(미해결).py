import sys
input = sys.stdin.readline
from collections import deque

def topology_sort():
    result = []
    q = deque()

    for i in range(1,V+1):
        if indegree[i]==0:
            q.append(i)
            ans1.append(live[i])

    while q:
        now = q.popleft()
        result.append(live[now])
        for i in graph[live[now]]:
            if live[now]=="sangdo":
                print(ans2)
                print("x")

            ans2[now].append(live2[i])
            for k in ans2[now]:
                if k in ans2[live2[i]]:
                    ans2[now].remove(k)
                if live2[i] in ans2[k]:
                    ans2[now].remove(live2[i])

            indegree[live2[i]]-=1
            if indegree[live2[i]]==0:
                q.append(live2[i])

    return result

V = int(input())
live = ["0"]+list(input().split())
live.sort()

live2 = {}
for i in range(1,V+1):
    live2[live[i]] = i
E = int(input())
indegree= [0]*(V+1)
graph = {}
for i in live:
    graph[i] = []


for i in range(E):
    b,a = input().split()
    graph[a].append(b)
    indegree[live2[b]] += 1


ans1=[]
ans2= [[] for i in range(V+1)]

topology_sort()
ans1.sort()

print(len(ans1))
print(*ans1)
print(live)
print(ans2)