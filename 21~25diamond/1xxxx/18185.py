import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

ans = 0

for i in range(n-2):
    if arr[i]==0:
        continue

    if arr[i+1]>arr[i+2]:
        t = min(arr[i], arr[i + 1] - arr[i + 2])
        ans += t * 5

        arr[i] -= t
        arr[i + 1] -= t

        if arr[i] == 0:
            continue


    t = min(arr[i],arr[i+1],arr[i+2])
    ans+= t*7
    arr[i] -= t
    arr[i+1] -= t
    arr[i+2] -= t

    if arr[i]==0:
        continue
    else:
        if arr[i+1]==0:
            ans += arr[i]*3
            arr[i] = 0
        else:
            s = min(arr[i],arr[i+1])
            m = max(arr[i],arr[i+1])

            ans += s*5
            ans += (m-s)*3
            arr[i] = 0
            arr[i+1] = 0



x = arr[-2]
y = arr[-1]

s = min(x,y)
m = max(x,y)
ans += s*5
ans += (m-s)*3

print(ans)