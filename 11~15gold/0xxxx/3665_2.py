import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    t = list(map(int,input().split()))
    graph = [set() for i in range(n+1)]
    indegree = [0]*(n+1)
    for i in range(n):
        for j in range(i+1,n):
            graph[t[i]].add(t[j])
            indegree[t[j]] += 1
    m = int(input())
    for __ in range(m):
        a,b = map(int,input().split())
        if b in graph[a]:
            graph[a].remove(b)
            graph[b].add(a)
            indegree[a]+=1
            indegree[b]-=1
        else:
            graph[b].remove(a)
            graph[a].add(b)
            indegree[b]+=1
            indegree[a]-=1
            
    q= []
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
    
    flag = 0
    ans = []
    while(q):
        if len(q)>1:
            flag = 1
            break
        t = q.pop()
        ans.append(t)
        for i in graph[t]:
            indegree[i] -= 1
            if indegree[i]==0:
                q.append(i)
    if flag==1:
        print("?")
    else:
        if len(ans)!=n:
            print("IMPOSSIBLE")
        else:
            print(*ans)