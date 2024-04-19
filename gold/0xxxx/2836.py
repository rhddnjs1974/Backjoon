import sys
input = sys.stdin.readline

n,m = map(int,input().split())

arr = []

for i in range(n):
    a,b = map(int,input().split())
    if a>b:
        arr.append((b,a))

t = 0
if arr:
    arr.sort()
    start = arr[0][0]
    end = arr[0][1]
    ans = 0
    for a,b in arr[1:]:

        if a>end:
            ans+=(end-start)
            start = a
            end = b
        else:
            end = max(end,b)

    t = ans+end-start

print(m+t*2)