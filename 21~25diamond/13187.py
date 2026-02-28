import sys
input = sys.stdin.readline

MOD = 1000000007

def comb(a, b):
    if (b < 0) or (b > a):
        return 0
    return (((fac[a] * invfac[b]) % MOD) * invfac[a - b]) % MOD


H, W = map(int, input().split())

inv2 = ((MOD + 1) // 2)
n = max(H, W)


fac = [1] * (n + 1)
for i in range(1, n + 1):
    fac[i] = ((fac[i - 1] * i) % MOD)

invfac = [1] * (n + 1)
invfac[n] = pow(fac[n], (MOD - 2), MOD)
for i in range(n, 0, -1):
    invfac[i - 1] = ((invfac[i] * i) % MOD)

inv2pow = [1] * (n + 1)
for i in range(1, n + 1):
    inv2pow[i] = ((inv2pow[i - 1] * inv2) % MOD)

gW = [0] * (H + 1)
for r in range(1, H + 1):
    gW[r] = ((pow(((1 + inv2pow[r]) % MOD), W, MOD) - 1) % MOD)

gH = [0] * (W + 1)
for c in range(1, W + 1):
    gH[c] = ((pow(((1 + inv2pow[c]) % MOD), H, MOD) - 1) % MOD)


Erow = 0
for r1 in range(1, H + 1):
    for r2 in range(1, (H - r1) + 1):
        x = ((comb(H, r1) * comb((H - r1), r2)) % MOD)
        Erow = (Erow + (((x * gW[r1]) % MOD) * gW[r2]) % MOD) % MOD

Ecol = 0
for c1 in range(1, W + 1):
    for c2 in range(1, (W - c1) + 1):
        x = ((comb(W, c1) * comb((W - c1), c2)) % MOD)
        Ecol = (Ecol + (((x * gH[c1]) % MOD) * gH[c2]) % MOD) % MOD

Eboth = 0
for u in range(1, W):
    cu = comb(W, u)
    p1au = pow(((1 + inv2pow[u]) % MOD), H, MOD)
    for v in range(1, (W - u) + 1):
        x = ((cu * comb((W - u), v)) % MOD)
        y = ((pow(((1 + inv2pow[u] + inv2pow[v]) % MOD), H, MOD) - p1au - pow(((1 + inv2pow[v]) % MOD), H, MOD) + 1) % MOD)
        
        Eboth = (Eboth + ((x * y) % MOD)) % MOD

ans = ((Erow + Ecol - Eboth) % MOD)
print(ans)