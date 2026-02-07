import sys
from bisect import bisect_right

input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

vals = sorted(A)
rank = {}
for i in range(N):
    rank[vals[i]] = i + 1

bit = [0] * (N + 1)

def bit_add(i, delta):
    while i <= N:
        bit[i] += delta
        i += i & -i

def bit_sum(i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

bit_add(rank[A[0]], 1)

cum = 0
found_idx = -1
t_in_step = 0

for i in range(1, N):
    r = rank[A[i]]
    leq = bit_sum(r)
    s = i - leq

    if s > 0:
        changes = s + 1
    else:
        changes = 0

    if cum + changes >= K:
        found_idx = i
        t_in_step = K - cum
        break

    cum += changes
    bit_add(r, 1)

if found_idx == -1:
    print(-1)
else:
    i = found_idx
    x = A[i]

    B = sorted(A[:i])
    pos = bisect_right(B, x)
    s = i - pos

    if t_in_step <= s:
        C = B + [x]
        loc = i - 1
        cnt = 0
        while cnt < t_in_step:
            C[loc + 1] = C[loc]
            loc -= 1
            cnt += 1
        ans = C + A[i+1:]
        print(*ans)
    else:
        C = sorted(A[:i+1])
        ans = C + A[i+1:]
        print(*ans)
