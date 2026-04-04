import sys
input = sys.stdin.readline

def push_stack(stack, ma, h):
    stk = list(stack)
    acc = 0
    while stk and stk[-1][0] >= h:
        sh, sw = stk.pop()
        ma = max(ma, sh * (sw+acc))
        acc += sw
    stk.append((h, acc+1))
    return tuple(stk), ma

def finalize(stack, ma):
    stk = list(stack)
    acc = 0
    while stk:
        sh, sw = stk.pop()
        acc += sw
        ma = max(ma, sh * acc)
    return ma

MOD = 998244353
n, m = map(int, input().split())
p = list(map(int, input().split()))

inv100 = pow(100, MOD-2, MOD)

comb = [[0] * (m+1) for _ in range(m+1)]
comb[0][0] = 1
for i in range(1, m+1):
    comb[i][0] = 1
    for j in range(1, i+1):
        comb[i][j] = (comb[i-1][j-1]+comb[i-1][j]) % MOD

prob = []
for i in range(n):
    a = p[i] * inv100 % MOD
    b = (1-a) % MOD
    row = []
    for h in range(m+1):
        v = comb[m][h]
        v = v * pow(a, h, MOD) % MOD
        v = v * pow(b, m-h, MOD) % MOD
        row.append(v)
    prob.append(row)

dp = {((), 0): 1}

for i in range(n):
    ndp = {}
    for (stack, ma), pr in dp.items():
        for h in range(m+1):
            ph = prob[i][h] * pr % MOD
            if ph == 0:
                continue
            nstack, nma = push_stack(stack, ma, h)
            key = (nstack, nma)
            ndp[key] = (ndp.get(key, 0)+ph) % MOD
    dp = ndp

ans = 0
for (stack, ma), pr in dp.items():
    ans += finalize(stack, ma) * pr % MOD
ans %= MOD

print(ans)