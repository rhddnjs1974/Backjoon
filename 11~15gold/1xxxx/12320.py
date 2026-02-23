import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    x, y = map(int,input().split())

    n = 0
    while True:
        n += 1
        s = n*(n+1)//2
        if s >= abs(x)+abs(y) and (s-(x+y))%2 == 0:
            break

    arr = ['']*(n+1)

    for k in range(n,0,-1):
        if abs(x) >= abs(y):
            if x >= 0:
                arr[k] = 'E'
                x -= k
            else:
                arr[k] = 'W'
                x += k
        else:
            if y >= 0:
                arr[k] = 'N'
                y -= k
            else:
                arr[k] = 'S'
                y += k

    ans = ""
    for i in range(1,n+1):
        ans += arr[i]

    print("Case #"+str(tc)+":",ans)