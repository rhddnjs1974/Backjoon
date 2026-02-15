import sys
input = sys.stdin.readline

def avg_distinct_prime_factors(x):
    s = 0
    c = 0
    last = 0
    while x > 1:
        p = spf[x]
        if p != last:
            s += p
            c += 1
            last = p
        x //= p
    return s / c

N, M = map(int, input().split())
A = list(map(int, input().split()))

diff = [0] * (N + 2)
for _ in range(M):
    l, r = map(int, input().split())
    diff[l - 1] += 1
    diff[r] -= 1

MAXA = 500000
spf = [0] * (MAXA + 1)
for i in range(2, MAXA + 1):
    if spf[i] == 0:
        spf[i] = i
        if i * i <= MAXA:
            for j in range(i * i, MAXA + 1, i):
                if spf[j] == 0:
                    spf[j] = i

cur = 0
ans = 0.0
for i in range(N):
    cur += diff[i]
    if cur > 0:
        ans += avg_distinct_prime_factors(A[i])
    else:
        ans += A[i]

print(ans)
