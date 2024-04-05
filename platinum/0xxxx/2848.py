import sys
input = sys.stdin.readline
from collections import deque

def topology_sort():
    global flag
    result = []
    q = deque()

    for i in range(27):
        if indegree[i]==0 and see[i]==1:
            q.append(i)
    if len(q)>1:
        flag=1


    while q:
        if len(q)>1:
            flag=1

        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)

    return result

flag = 0
flag2=0
indegree= [0]*(27)
graph = [[] for i in range(27)]
see = [0]*27

N = int(input())
arr=[]
for i in range(N):
    x = input().rstrip()
    for k in x:
        see[ord(k)-97]=1
    for j in arr:
        t = 0
        while(j[t]==x[t] and len(j)>t+1 and len(x)>t+1):
            t+=1
        if (ord(x[t])-97) not in graph[ord(j[t])-97] and (ord(x[t])-97)!=ord(j[t])-97:
            graph[ord(j[t])-97].append(ord(x[t])-97)
            indegree[ord(x[t])-97] += 1
        if (ord(x[t])-97)==ord(j[t])-97 and len(x)<len(j):
            flag2=1
    arr.append(x)

ans = topology_sort()

if len(ans)!=sum(see) or flag2==1:
    print("!")
elif flag==1:
    print("?")
else:
    for i in ans:
        print(chr(i+97),end="")
