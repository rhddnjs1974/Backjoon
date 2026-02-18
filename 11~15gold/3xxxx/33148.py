import sys
import math

input = sys.stdin.readline

N = int(input())
M = list(map(int, input().split()))

if len(M) != N*N:
    print("NO")
    sys.exit(0)

M.sort()

cnt = {}
for t in M:
    if t in cnt:
        cnt[t] += 1
    else:
        cnt[t] = 1

idx = 0

def next_min():
    global idx
    while idx < len(M) and cnt[M[idx]] == 0:
        idx += 1
    if idx == len(M):
        return -1
    return M[idx]

first_val = next_min()
if first_val == -1:
    print("NO")
    sys.exit(0)

x = math.isqrt(first_val)
if x * x != first_val:
    print("NO")
    sys.exit(0)

c0 = cnt[first_val]
m = math.isqrt(c0)
if m * m != c0:
    print("NO")
    sys.exit(0)

A = [x] * m
vals = [x]
mult = [m]

cnt[first_val] = 0

while len(A) < N:
    t = next_min()
    if t == -1:
        print("NO")
        sys.exit(0)

    if t % x != 0:
        print("NO")
        sys.exit(0)

    v = t // x

    c = cnt[t]
    denom = 2 * m
    if c % denom != 0:
        print("NO")
        sys.exit(0)

    mv = c // denom
    if mv <= 0:
        print("NO")
        sys.exit(0)

    for i in range(len(vals)):
        u = vals[i]
        mu = mult[i]
        prod = u * v
        need2 = 2 * mu * mv
        if prod not in cnt or cnt[prod] < need2:
            print("NO")
            sys.exit(0)
        cnt[prod] -= need2

    vv = v * v
    need1 = mv * mv
    if vv not in cnt or cnt[vv] < need1:
        print("NO")
        sys.exit(0)
    cnt[vv] -= need1

    A += [v] * mv
    vals.append(v)
    mult.append(mv)

if len(A) != N:
    print("NO")
    sys.exit(0)

print("YES")
print(*A)
