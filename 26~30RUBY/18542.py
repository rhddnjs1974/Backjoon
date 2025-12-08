import sys
input = sys.stdin.readline
MOD = 10**9 + 7

def modinv(x):
    return pow(x, MOD - 2, MOD)

def trim(p):
    while p and p[-1] == 0:
        p.pop()
    return p

def degree(p):
    return len(p) - 1 

def poly_mod(F, G):
    F = F[:]      
    G = trim(G[:])
    if not G:
        exit() #error
    inv_lcG = modinv(G[-1])

    while len(F) >= len(G) and F:
        coef = F[-1] * inv_lcG % MOD
        shift = len(F) - len(G)
        for i in range(len(G)):
            F[shift + i] = (F[shift + i] - coef * G[i]) % MOD
        trim(F)

    return F


def resultant_mod(F, G):
    F = trim(F[:])
    G = trim(G[:])

    if not F or not G:
        return 0

    res = 1

    while degree(G) > 0:
        R = poly_mod(F, G)
        if not R:
            return 0

        dF = degree(F)
        dG = degree(G)
        dR = degree(R)

        lcG = G[-1] % MOD

        power = dF - dR
        res = res * pow(lcG, power, MOD) % MOD

        if (dR * dG) & 1:
            res = (-res) % MOD

        F, G = G, R

    c = G[0] % MOD
    dF = degree(F)
    res = res * pow(c, dF, MOD) % MOD
    return res

def cycle_decomposition(pi):
    n = len(pi)
    vis = [False] * n
    cycles = []
    for i in range(n):
        if not vis[i]:
            cyc = []
            cur = i
            while not vis[cur]:
                vis[cur] = True
                cyc.append(cur)
                cur = pi[cur]
            cycles.append(cyc)
    return cycles

def permutation_sign_from_order(order):
    inv_parity = 0
    n = len(order)
    for i in range(n):
        oi = order[i]
        for j in range(i + 1, n):
            if oi > order[j]:
                inv_parity ^= 1
    return -1 if inv_parity else 1

n = int(input().strip())
a = list(map(int, input().split()))
a = [x % MOD for x in a]
pi = list(map(int, input().split()))
pi = [x - 1 for x in pi]

cycles = cycle_decomposition(pi)

if len(cycles) != 1:
    print(0)
    exit()

cycle = cycles[0] 

start = cycle[0]
order = [start]
cur = pi[start]
while cur != start:
    order.append(cur)
    cur = pi[cur]

f = [a[idx] for idx in order]

g = [0] * (n + 1)
g[0] = (MOD - 1)
g[n] = 1

res = resultant_mod(g, f)
if res == 0:
    print(0)
    exit()

sign_perm = permutation_sign_from_order(order) 

if n % 4 in (1, 2):
    s_n = 1
else:
    s_n = -1

sign_total = sign_perm * s_n
if sign_total == -1:
    res = (-res) % MOD

print(res % MOD)

