def match(N):
    if visit[N]!=0:
        return 0
    visit[N] = 1

    for x in graph[N]:
        if connect[x] == -1 or match(connect[x])==1:
            connect[x] = N
            return 1

    return 0

N, M = map(int,input().split())
dic = {}
for i in range(M):
    a = input()
    dic[a] = i

ans = [0]*M

graph = []
for i in range(N):
    x = list(input().split())
    x[0] = int(x[0])
    for j in range(1,len(x)):
        x[j] = dic[x[j]]
    y = x[1:]
    y.sort()
    graph.append(y)


connect = [-1]*(M)

for i in range(N):
    visit = [0]*(N)
    match(i)

ans = 0
for i in range(M):
    if connect[i]!=-1:
        ans+=1

if ans==N:
    print("YES")
else:
    print("NO")
    print(ans)