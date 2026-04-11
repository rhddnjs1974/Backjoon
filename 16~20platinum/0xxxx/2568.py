import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
pairs = []
for _ in range(n):
    a, b = map(int, input().split())
    pairs.append((a, b))

pairs.sort()

tails = []
tails_idx = []
prev = [-1] * n

for i in range(n):
    b = pairs[i][1]
    idx = bisect_left(tails, b)
    if idx == len(tails):
        tails.append(b)
        tails_idx.append(i)
    else:
        tails[idx] = b
        tails_idx[idx] = i
    if idx > 0:
        prev[i] = tails_idx[idx-1]

lis_set = [False] * n
cur = tails_idx[-1]
while cur != -1:
    lis_set[cur] = True
    cur = prev[cur]

print(n-len(tails))
for i in range(n):
    if not lis_set[i]:
        print(pairs[i][0])
