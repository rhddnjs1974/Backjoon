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

n = int(input())

arr = []
for i in range(n):
    size,speed,brain = map(int,input().split())
    arr.append((size,speed,brain,i))


graph = []
for i in range(n*2):
    graph.append([])

for i in range(n):
    for j in range(n):
        if arr[i][0]>=arr[j][0] and arr[i][1]>=arr[j][1] and arr[i][2]>=arr[j][2]:
            if arr[i][0]==arr[j][0] and arr[i][1]==arr[j][1] and arr[i][2]==arr[j][2] and arr[i][3]<=arr[j][3]:
                continue
            graph[i].append(j)
            graph[i+n].append(j)



connect = [-1]*(n*2)

for i in range(n*2):
    visit = [0]*(n*2)
    match(i)

ans = 0
for i in range(n*2):
    if connect[i]!=-1:
        ans+=1


print(n-ans)