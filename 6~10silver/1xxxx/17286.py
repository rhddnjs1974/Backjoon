x,y = map(int,input().split())

arr = []
for i in range(3):
    a,b = map(int,input().split())
    arr.append((a,b))
    
ff = [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]

ans = 1e9
for route in ff:
    xx = x
    yy = y
    dist = 0
    for now in route:
        a,b = arr[now]
        dist += ((xx-a)**2 + (yy-b)**2 )**0.5
        xx = a
        yy = b
    ans = min(ans,dist)

print(int(ans))