import sys
input = sys.stdin.readline

N,M,H = map(int,input().split())

arr= []
for i in range(N):
    arr.append(list(map(int,input().split())))

mint = [0]
for i in range(N):
    for j in range(N):
        if arr[i][j]==1:
            house = (i,j)
        if arr[i][j]==2:
            mint.append((i,j))

l = len(mint)
graph = [[]for i in range(l)]

for i in range(1,l):
    graph[0].append((i,abs(house[0]-mint[i][0])+abs(house[1]-mint[i][1])))
    graph[i].append((0,abs(house[0]-mint[i][0])+abs(house[1]-mint[i][1])))

    
    
for i in range(1,l):
    for j in range(1,l):
        if i==j:
            continue
        graph[i].append((j,abs(mint[j][0]-mint[i][0])+abs(mint[j][1]-mint[i][1])))

def bt(now,hp,num):
    global ans,l
    if now==0 and num!=0:
        ans=max(ans,num)
        return
    
    for i,dist in graph[now]:
        if dist>hp:
            continue
        if visit[i]==1:
            continue
        visit[i]=1
        bt(i,hp-dist+H,num+1)
        visit[i]=0

ans = 1
visit = [0]*l
bt(0,M,0)


print(ans-1)