import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int,input().split()))
    now = 0
    misum = 0

    ans = -1e9

    for i in arr:
        now +=i
        ans = max(ans,now-misum)
        misum = min(misum,now)


    print(ans)