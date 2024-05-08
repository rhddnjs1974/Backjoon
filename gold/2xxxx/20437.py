import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    ans1 = 1e9
    ans2 = 0

    w = input().rstrip()
    k = int(input())

    arr = []
    for i in range(26):
        arr.append(deque())


    if k==1:
        print(1,1)
    else:
        for i in range(len(w)):
            x = ord(w[i])-97
            if len(arr[x])==k-1:
                t = arr[x].popleft()
                arr[x].append(i)

                ans1 = min(ans1,i-t+1)
                ans2 = max(ans2,i-t+1)
            else:
                arr[x].append(i)

        if ans2==0:
            print(-1)
        else:
            print(ans1,ans2)