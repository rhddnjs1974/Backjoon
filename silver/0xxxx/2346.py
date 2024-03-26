import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

arr = list(map(int,input().split()))
arr2 = []
for i in range(n):
    arr2.append((i,arr[i]))
q = deque(arr2)

ans = []

while(len(q)>0):
    index,t = q.popleft()
    ans.append(index)

    if q:
        if t>0:
            for i in range(t-1):
                q.append(q.popleft())
        else:
            for i in range(-t):
                q.appendleft(q.pop())

for i in ans:
    print(i+1,end=" ")