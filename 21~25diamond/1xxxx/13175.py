import sys
input = sys.stdin.readline

MOD = 1000000007
BASE = 1000000000

N = int(input().strip())

p = [0] * N
d = [0] * N

inv_base = pow(BASE, MOD - 2, MOD)

for i in range(N):
    pi, di = map(int, input().split())
    p[i] = (pi % MOD) * inv_base % MOD
    d[i] = di % MOD

c = [0] * (N + 1)
c[0] = 1
for i in range(N):
    for k in range(N,0,-1):
        c[k] = (c[k] - p[i] * c[k - 1]) % MOD

inv = [0] * (N + 1)
for k in range(1,N+1):
    inv[k] = pow(k, MOD - 2, MOD)

ans = 0

for i in range(N):
    a_pre = 1
    I = a_pre * inv[1] % MOD

    k = 1
    while k <= N - 1:
        a_cur = (c[k] + p[i] * a_pre) % MOD
        I = (I + a_cur * inv[k + 1]) % MOD
        a_pre = a_cur
        k += 1

    ans = (ans + ((d[i] * p[i]) % MOD) * I) % MOD

print(ans)