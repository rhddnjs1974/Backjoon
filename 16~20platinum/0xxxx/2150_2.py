import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def scc(x):
    global now
    now +=1
    visit[x] = now
    parent = now
    q.append(x)
    for i in graph[x]:
        if visit[i]==0:
            parent = min(parent,scc(i))
        elif finish[i] == 0:
            parent = min(parent,visit[i])
    
    if parent == visit[x]:
        scc_arr.append([])
        while(q):
            s = q.pop()
            finish[s] = 1
            scc_arr[-1].append(s)
            if s==x:
                break
    
    return parent
    

V,E = map(int,input().split())
graph = [[] for i in range(V+1)]

for _ in range(E):
    a,b = map(int,input().split())
    graph[a].append(b)
    
q = []
visit = [0]*(V+1)
finish = [0]*(V+1)
now =0
scc_arr = []
for i in range(1,V+1):
    if visit[i]==0:
        scc(i)

print(len(scc_arr))

for i in range(len(scc_arr)):
    scc_arr[i].sort()
scc_arr.sort()

for i in scc_arr:
    print(*i,end=" -1\n")