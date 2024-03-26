import sys
input = sys.stdin.readline
from collections import deque

q = deque()
N = int(input())
for i in range(1,N+1):
    q.append(i)

t = 1
while(len(q)>1):
    if t%2==1:
        q.popleft()
    else:
        q.append(q.popleft())
    t+=1

print(q[0])