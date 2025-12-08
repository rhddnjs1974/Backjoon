import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    a,b = map(int,input().split())
    arr.append((a,b))

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

print(ans+end-start)