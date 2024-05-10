import copy
import sys
input = sys.stdin.readline

def match(N):
    if visit[N]!=0:
        return 0
    visit[N] = 1

    for x in graph[N]:
        if connect[x] == -1 or match(connect[x])==1:
            connect[x] = N

            return 1

    return 0


def primeList(n):
    n+=1
    arr = [0,0] + [1]*n

    for i in range(2,int(n**0.5)+1):
        if arr[i]==1:
            for j in range(i*2,n+1,i):
                arr[j] = 0

    return arr

prime_list = primeList(2001)


n = int(input())
arr = list(map(int,input().split()))
graph = []
for i in range(n):
    graph.append([])
for i in range(n):
    for j in range(i+1,n):
        if prime_list[arr[i]+arr[j]]==1:
            graph[i].append(j)
            graph[j].append(i)



graph_t = copy.deepcopy(graph[0])

ans2 = []

for s in graph_t:
    graph[0]=[s]

    connect = [-1]*(n)

    for i in range(n):
        visit = [0]*(n)
        match(i)

    ans = 0
    for i in range(n):
        if connect[i]!=-1:
            ans+=1

    if -1 not in connect:
        ans2.append(arr[s])

if len(ans2)==0:
    print(-1)
else:
    ans2.sort()
    print(*ans2)