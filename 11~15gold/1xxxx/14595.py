import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = []
for i in range(m):
    x,y = map(int,input().split())
    arr.append((x,y))

arr.sort()

t = 0
ans = 0

for i in range(m):

    a,b = arr[i]
    if a<=t:
        t = max(b,t)
    else:
        ans += (a-t)

    t = max(b,t)
ans += n-t
print(ans)