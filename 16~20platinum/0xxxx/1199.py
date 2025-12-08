
N = int(input())

graph = []

for i in range(1,N+1):
    graph.append(list(map(int,input().split())))

odd = []
for i in range(N):
    x= 0
    for j in graph[i]:
        x+=j
    if x%2!=0:
        odd.append(i)

if len(odd)==0 or len(odd)==2:
    if len(odd)==0:
        stack = [0]
    else:
        stack = [odd[0]]
    path = []
    while stack:
        v = stack[-1]
        for i in range(N):
            if graph[v][i]!=0:
                stack.append(i)
                graph[v][i]-=1
                graph[i][v]-=1
                break
            if i==N-1:
                path.append(stack.pop())

    for x in path[::-1]:
        print(str(x+1),end=" ")
else:
    print(-1)