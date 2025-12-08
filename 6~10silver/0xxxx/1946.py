import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    n = int(input())
    arr=[]
    for j in range(n):
        a,b = map(int,input().split())
        arr.append((a,b))
    arr.sort()
    mi = 1e7
    ans=0
    for x,y in arr:
        if y<mi:
            ans+=1
            mi = y
    print(ans)