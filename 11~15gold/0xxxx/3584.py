import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N = int(input())
    parent = [0]*(N+1)
    for j in range(N-1):
        a,b = map(int,input().split())
        parent[b] = a

    x,y = map(int,input().split())
    x_parent = [0,x]
    y_parent = [0,y]

    while parent[x]:
        x_parent.append(parent[x])
        x = parent[x]
    while parent[y]:
        y_parent.append(parent[y])
        y = parent[y]

    i = 1
    while x_parent[-i]==y_parent[-i]:
        i+=1

    print(x_parent[-i+1])
