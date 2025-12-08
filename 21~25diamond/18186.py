import sys
input = sys.stdin.readline

n,b,c = map(int,input().split())
arr = list(map(int,input().split()))

price3 = b+2*c
price2 = b+c
price1 = b

if c<b:
    ans = 0

    for i in range(n-2):
        if arr[i]==0:
            continue

        if arr[i+1]>arr[i+2]:
            t = min(arr[i], arr[i + 1] - arr[i + 2])
            ans += t * price2

            arr[i] -= t
            arr[i + 1] -= t

            if arr[i] == 0:
                continue


        t = min(arr[i],arr[i+1],arr[i+2])
        ans+= t* price3
        arr[i] -= t
        arr[i+1] -= t
        arr[i+2] -= t

        if arr[i]==0:
            continue
        else:
            if arr[i+1]==0:
                ans += arr[i]* price1
                arr[i] = 0
            else:
                s = min(arr[i],arr[i+1])
                m = max(arr[i],arr[i+1])

                ans += s*price2
                ans += (m-s)*price1
                arr[i] = 0
                arr[i+1] = 0

    x = arr[-2]
    y = arr[-1]

    s = min(x,y)
    m = max(x,y)
    ans += s*price2
    ans += (m-s)*price1

    print(ans)

else:
    t = sum(arr)
    print(t*b)