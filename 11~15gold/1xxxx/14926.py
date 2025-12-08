import sys
input = sys.stdin.readline
########################################


N = int(input())

graph = [[0]*(N+1) for i in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        if i!=j:
            graph[i][j] = 1    

#for i in range(1,N+1):
#    graph[i].reverse()

stack = [1]
path = []
while stack:
    v = stack[-1]
    for i in range(1,N+1):
        if graph[v][i]==1:
            stack.append(i)
            graph[v][i]=0
            graph[i][v]=0
            break
        if i==N:
            path.append(stack.pop())

for x in path[::-1]:
    print("a"+str(x),end=" ")