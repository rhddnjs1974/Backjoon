from collections import deque
n = int(input())

a = deque()
for i in range(1,n+1):
    a.append(i)

arr = []
while(a):
    arr.append(a.popleft())
    if len(a)==0:
        break
    a.append(a.popleft())

print(*arr)