import sys
input = sys.stdin.readline
from collections import deque

N,K = map(int,input().split())
q = deque()

for i in range(1,N+1):
    q.append(i)

ans = []

while(q):
    t = 0
    while(t<K-1):
        t+=1
        q.append(q.popleft())
    ans.append(q.popleft())

print("<",end="")
for i in range(N-1):
    print(ans[i],end=", ")
print(ans[-1],end=">")