import sys
input = sys.stdin.readline
from collections import deque

q = deque()

n = int(input())
for i in range(n):
    a = input().rstrip()
    if a=="3":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif a=="4":
        if q:
            print(q.pop())
        else:
            print(-1)
    elif a=="5":
        print(len(q))
    elif a=="6":
        if q:
            print(0)
        else:
            print(1)
    elif a=="7":
        if q:
            print(q[0])
        else:
            print(-1)
    elif a=="8":
        if q:
            print(q[-1])
        else:
            print(-1)
    else:
        b,c = a.split()
        if b=="1":
            q.appendleft(c)
        else:
            q.append(c)
