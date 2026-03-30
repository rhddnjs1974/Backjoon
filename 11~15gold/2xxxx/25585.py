from collections import deque
N = int(input())
region = []

odd = 0
even = 0

for i in range(N):
    arr = list(map(int,input().split()))
    for j in range(N):
        if arr[j]==2:
            me = (i,j)
        if arr[j]==1:
            region.append((i,j))
            if (i+j)%2==0:
                even += 1
            else:
                odd += 1

if (me[0]+me[1])%2==0:
    if odd>0:
        print("Shorei")
        exit()
else:
    if even>0:
        print("Shorei")
        exit()


graph = [[] for i in range(len(region)+1)]

for i in range(len(region)):
    dist = max(abs(me[0]-region[i][0]),abs(me[1]-region[i][1]))
    graph[0].append((i+1,dist))

for i in range(len(region)):
    for j in range(i+1,len(region)):
        if i==j:
            continue
        dist = max(abs(region[j][0]-region[i][0]),abs(region[j][1]-region[i][1]))
        graph[i+1].append((j+1,dist))
        graph[j+1].append((i+1,dist))


def bt(idx,now,nowdist):

    global ans
    if now==len(region):
        ans = min(ans,nowdist)
        return

    for next,dist in graph[idx]:
        if visit[next]==1:
            continue
        visit[next] = 1
        bt(next,now+1,nowdist+dist)
        visit[next] = 0
        
visit = [0]*(len(region)+1)
visit[0] = 1
ans = 1e9
bt(0,0,0)

print("Undertaker")
print(ans)