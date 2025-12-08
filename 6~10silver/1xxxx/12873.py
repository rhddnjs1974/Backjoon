from collections import deque
n = int(input())
q = deque()

for i in range(1,n+1):
    q.append(i)

for level in range(1,n):

    for j in range( ((level**3)-1)%len(q)  ):
        t = q.popleft()
        q.append(t)
    trash = q.popleft()

print(q[0])