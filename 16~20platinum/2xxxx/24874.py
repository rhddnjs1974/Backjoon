import sys
input = sys.stdin.readline

MOD = 10**9+7
NM = 2 * 10**5 + 10

def C(n, k):
    if k < 0 or k > n or n < 0:
        return 0
    return fa[n] * ifa[k] % MOD * ifa[n-k] % MOD

def F0(m_00, m_11, k):
    if k == 0:
        if m_11 == 0:
            return 1
        return 0
    return C(m_00+k, k) * C(m_11+k-1, k-1) % MOD

def F1(m_00, m_11, k):
    return C(m_00+k, k) * C(m_11+k, k) % MOD

fa = [1] * NM
for i in range(1, NM):
    fa[i] = fa[i-1] * i % MOD
ifa = [1] * NM
ifa[NM-1] = pow(fa[NM-1], MOD-2, MOD)
for i in range(NM-2, -1, -1):
    ifa[i] = ifa[i+1] * (i+1) % MOD

a = input().rstrip()
b = input().rstrip()
c = input().rstrip()
n = len(a)

n_00 = 0
n_01 = 0
n_10 = 0
n_11 = 0
g_00 = 0
g_10 = 0
ok = True

for i in range(n):
    da = int(a[i])
    db = int(b[i])
    dc = int(c[i])
    s = da+db
    if s == dc:
        n_00 += 1
        if da != 0 and db != 0:
            g_00 += 1
    elif s+1 == dc:
        n_10 += 1
        if da != 0 and db != 0:
            g_10 += 1
    elif s-10 == dc:
        n_01 += 1
    elif s-9 == dc:
        n_11 += 1
    else:
        ok = False
        break

if not ok or n_01 != n_10:
    print(0)
else:
    ans = 0
    if g_00 > 0:
        f0v = F0(n_00-1, n_11, n_01)
        mult = fa[n_00-1] * fa[n_01] % MOD * fa[n_10] % MOD * fa[n_11] % MOD
        ans = (ans+g_00 * f0v % MOD * mult) % MOD
    if g_10 > 0:
        f1v = F1(n_00, n_11, n_10-1)
        mult = fa[n_00] * fa[n_01] % MOD * fa[n_10-1] % MOD * fa[n_11] % MOD
        ans = (ans+g_10 * f1v % MOD * mult) % MOD
    print(ans)
