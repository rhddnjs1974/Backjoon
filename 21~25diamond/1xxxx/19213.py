
MOD = 1000000007

n = int(input())

if n == 0:
    print(0)
else:
    E = 1
    M = 1

    P = 1
    R = 1

    S2 = 1

    for k in range(1, n + 1):
        inv_k = pow(k, MOD - 2, MOD)
        inv_k2 = (inv_k * inv_k) % MOD

        E_k = (2 * P) % MOD
        E_k = (E_k * inv_k) % MOD

        term1 = (2 * R) % MOD
        term1 = (term1 * inv_k) % MOD

        term2 = (2 * S2) % MOD
        term2 = (term2 * inv_k2) % MOD

        M_k = term1 + term2
        M_k %= MOD

        factor = (1 + (4 * inv_k) % MOD) % MOD
        S2 = (S2 * factor + M_k) % MOD

        P = (P + E_k) % MOD
        R = (R + M_k) % MOD

        E = E_k
        M = M_k

    var = (M - (E * E) % MOD) % MOD
    print(var)
