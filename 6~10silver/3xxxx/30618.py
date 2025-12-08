import sys
from collections import deque

n = int(input())
q = deque()
q.append(n)
x = 1
for i in range(n-1,0,-1):
    x *= -1
    if x==1:
        q.append(i)
    else:
        q.appendleft(i)

q = list(q)
print(*q)