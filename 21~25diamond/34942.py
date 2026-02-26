import sys

input = sys.stdin.readline

MOD = 998244353

N = int(input().strip())
arr = list(map(int, input().split()))

pairs = []
for i in range(N):
    pairs.append((arr[i], i))
pairs.sort()

a = [0] * (N + 1)
pos = [0] * (N + 1)
for i in range(1, N + 1):
    a[i] = pairs[i - 1][0] % MOD
    pos[i] = pairs[i - 1][1]

inv_int = [0] * (N + 1)
inv_int[1] = 1
for i in range(2, N + 1):
    inv_int[i] = (MOD - (((MOD // i) * inv_int[MOD % i]) % MOD)) % MOD

suf = [0] * (N + 1)
suf[N] = 1
for m in range(N - 1, -1, -1):
    suf[m] = ((suf[m + 1] * a[m + 1]) % MOD)

inv_suf = [0] * (N + 1)
inv_suf[0] = pow(suf[0], (MOD - 2), MOD)
for m in range(0, N):
    inv_suf[m + 1] = ((inv_suf[m] * a[m + 1]) % MOD)

p = [0] * (N + 1)
for t in range(1, N + 1):
    p[t] = pow(a[t], (N - t), MOD)

ans = [0] * N

pref = 0
for k in range(1, N + 1):
    e = (N - k + 1)
    upper = ((p[k] * a[k]) % MOD)
    if k == 1:
        lower = 0
    else:
        lower = p[k - 1]
    diff = (upper - lower) % MOD
    term = (((diff * inv_int[e]) % MOD) * inv_suf[k - 1]) % MOD
    pref = (pref + term) % MOD
    ans[pos[k]] = pref

for i in range(N):
    print(ans[i])