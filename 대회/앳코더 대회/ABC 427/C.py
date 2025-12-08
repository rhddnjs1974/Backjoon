import sys
input = sys.stdin.readline

N, M = map(int,input().split())

edge = []

for i in range(M):
    u, v = map(int,input().split())
    edge.append((u,v))
    
mc = 0
for m in range(0,1<<N):
    if m&1 == 0:
        c=0
        for x,y in edge:
            if ((m>>x)&1) != ((m>>y)&1):
                c+=1
        mc = max(mc,c)
print(M-mc)