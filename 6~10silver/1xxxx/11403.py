import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
dist_array = []

for i in range(n):
    dist_array.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if dist_array[i][j] == 0:
            dist_array[i][j] = INF



for k in range(n):
    for i in range(n):
        for j in range(n):
            dist_array[i][j] = min(dist_array[i][j],dist_array[i][k]+dist_array[k][j])

for i in range(n):
    for j in range(n):
        if dist_array[i][j] == INF:
            print(0,end=" ")
        else:
            print(1,end=" ")
    print()
