MOD = 1000000007

def mod_inv(x):
    return pow(x, MOD-2, MOD)

inv3 = mod_inv(3)

import sys
input = sys.stdin.readline

Q = int(input())

for _ in range(Q):
    H, K = map(int, input().split())

    if H <= 1:
        print(0)
        continue

    if K == 1:
        ans = (H + 1) % MOD * inv3 % MOD
        print(ans)
        continue

    r = K % MOD
    inv = mod_inv(r - 1)

    p = pow(r, H, MOD)

    N = (p - 1) % MOD * inv % MOD

    S = (H - 1) % MOD * (p + 1) % MOD
    t = (p - r) % MOD
    S = (S - 2 * t % MOD * inv) % MOD

    inv2 = inv * inv % MOD
    D = p * S % MOD * inv2 % MOD

    ans = D * 2 % MOD
    ans = ans * mod_inv(N) % MOD
    ans = ans * mod_inv((N - 1) % MOD) % MOD

    print(ans)
