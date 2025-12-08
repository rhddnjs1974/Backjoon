arr = [[0]*100 for i in range(100)]

n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    for x in range(10):
        for y in range(10):
            try:
                arr[a+x][b+y]=1
            except:
                continue

ans = 0
for i in arr:
    ans+=sum(i)
print(ans)