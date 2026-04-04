import sys
input = sys.stdin.readline
from bisect import bisect_right

n = int(input())
b = list(map(int, input().split()))

segs = []
for i in range(1, n+1):
    bi = b[i-1]
    if (bi-i) % n <= (i-bi) % n:
        s, e = i, bi
    else:
        s, e = bi, i
    
    if s <= e:
        segs.append((s, e))
        segs.append((s+n, e+n))
    else:
        segs.append((s, e+n))

segs.sort(key=lambda x: (x[0], -x[1]))

tails = []
for _, e in segs:
    idx = bisect_right(tails, -e)
    if idx == len(tails):
        tails.append(-e)
    else:
        tails[idx] = -e

print(len(tails))