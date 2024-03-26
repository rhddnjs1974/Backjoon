import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

M = int(input())
C = list(map(int,input().split()))

q = deque()
for j in range(N):
    if A[j]==0:
        q.append(B[j])

for i in C:
    q.appendleft(i)
    print(q.pop(),end=" ")