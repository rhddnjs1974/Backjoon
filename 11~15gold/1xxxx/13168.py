import sys
input = sys.stdin.readline
INF = int(1e6)

n,R = map(int,input().split())
dosiset = set(list(input().split()))
dosi = {}
x=0
for i in dosiset:
    dosi[i]=x
    x+=1
R*=2
n = x

m = int(input())
plan = list(input().split())

dist_array = [[INF]*(n+1) for i in range(n+1)]
dist_array2 = [[INF]*(n+1) for i in range(n+1)]


for i in range(int(input())):
    a,b,c,d = input().split()
    d = int(d)
    d*=2
    b = dosi[b]
    c = dosi[c]
    
    if a=="S-Train" or a=="V-Train":
        dist_array[b][c] = min(dist_array[b][c],d)
        dist_array[c][b] = min(dist_array[c][b],d)

        dist_array2[b][c] = min(dist_array2[b][c],d//2)
        dist_array2[c][b] = min(dist_array2[c][b],d//2)    
    elif a=="Mugunghwa" or a=="ITX-Cheongchun" or a=="ITX-Saemaeul":
        dist_array[b][c] = min(dist_array[b][c],d)
        dist_array[c][b] = min(dist_array[c][b],d)

        dist_array2[b][c] = 0
        dist_array2[c][b] = 0
    else:
        dist_array[b][c] = min(dist_array[b][c],d)
        dist_array[c][b] = min(dist_array[c][b],d)

        dist_array2[b][c] = min(dist_array2[b][c],d)
        dist_array2[c][b] = min(dist_array2[c][b],d)
        
        
for i in range(n+1):
    dist_array[i][i] = 0

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            dist_array[i][j] = min(dist_array[i][j],dist_array[i][k]+dist_array[k][j])


for i in range(n+1):
    dist_array2[i][i] = 0

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            dist_array2[i][j] = min(dist_array2[i][j],dist_array2[i][k]+dist_array2[k][j])
            

cost1 = 0
cost2 = 0

for i in range(m-1):
    a = dosi[plan[i]]
    b = dosi[plan[i+1]]
    
    cost1 += dist_array[a][b]
    cost2 += dist_array2[a][b]


if cost2+R<cost1:
    print("Yes")
else:
    print("No")