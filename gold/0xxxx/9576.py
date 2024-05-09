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

T = int(input())
for _ in range(T):
    m,n = map(int,input().split())
    graph = []
    for i in range(n):
        a,b = map(int,input().split())
        graph.append([])
        for j in range(a,b+1):
            graph[i].append(j)

    connect = [-1]*(m+1)

    for i in range(n):
        visit = [0]*(n)
        match(i)

    ans = 0
    for i in range(1,m+1):
        if connect[i]!=-1:
            ans+=1

    print(ans)