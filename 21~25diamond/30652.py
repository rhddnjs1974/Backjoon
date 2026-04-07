import sys
input = sys.stdin.readline

def comb(n, r, fact, invfact):
    if r < 0 or r > n:
        return 0
    return fact[n] * invfact[r] % MOD * invfact[n-r] % MOD

MOD = 1000000007
n, k = map(int, input().split())

lim = min(n, k)

fact = [1] * (n+1)
for i in range(1, n+1):
    fact[i] = fact[i-1] * i % MOD

invfact = [1] * (n+1)
invfact[n] = pow(fact[n], MOD-2, MOD)
for i in range(n, 0, -1):
    invfact[i-1] = invfact[i] * i % MOD

part = [0] * (n-1)
part[0] = 1

ans = 0

for a in range(lim-1):
    m = a+2
    r = n-m
    val = 0
    for q in range(r+1):
        val += part[q] * comb((r-q)//2+a, a, fact, invfact)
        val %= MOD
    ans += (k-m+1) * (2 * val % MOD)
    ans %= MOD

    w = a+1
    for q in range(n-2, w-1, -1):
        part[q] += part[q-w]
        if part[q] >= MOD:
            part[q] -= MOD

print(ans % MOD)