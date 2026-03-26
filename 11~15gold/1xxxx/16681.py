import heapq
import sys
input = sys.stdin.readline

def dyik(x):
    heap = [(-E,x,1)] #1 : up 2 : down
    
    while(heap):
        nowdist, nownode, updown = heapq.heappop(heap)
        
        if dist1[nownode] < nowdist and updown==1:
            continue
        if dist2[nownode] < nowdist and updown==2:
            continue
        
        for nextnode,dist in graph[nownode]:
            if updown == 1 and H[nextnode]>H[nownode]: # 올라가는 중
                if dist1[nextnode] > nowdist + dist*D - (H[nextnode]-H[nownode])*E:
                    dist1[nextnode] = nowdist + dist*D - (H[nextnode]-H[nownode])*E
                    heapq.heappush(heap,(dist1[nextnode],nextnode,1))

            elif H[nextnode]<H[nownode]: # 내려가는 중
                if dist2[nextnode] > nowdist + dist*D:
                    dist2[nextnode] = nowdist + dist*D
                    heapq.heappush(heap,(dist2[nextnode],nextnode,2))
    
    return

N,M,D,E = map(int,input().split())
H = [0]+list(map(int,input().split()))
graph = [[] for i in range(N+1)]
for i in range(M):
    a,b,n = map(int,input().split())
    graph[a].append((b,n))
    graph[b].append((a,n))
inf = 1e14

dist1 = [inf]*(N+1) # 올라가는 중
dist2 = [inf]*(N+1) # 내려오는 중

dist1[1] = -E

dyik(1)

if dist2[-1]>1e13:
    print("Impossible")
else:
    print(-dist2[-1])