import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    ans1 = 1e9

    w = input().rstrip()
    k = int(input())

    arr = [-1]*26

    for i in range(len(w)):
        x = ord(w[i])-97
        if arr[x]==-1:
            arr[x] = i
        else:
            ans1 = min(ans1,i-arr[x]+1)
            arr[x] = i

    print(ans1)