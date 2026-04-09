MOD = 1000000007

def mod_pow(a, b, mod=MOD):
    a %= mod
    res = 1
    while b > 0:
        if b & 1:
            res = (res * a) % mod
        a = (a * a) % mod
        b >>= 1
    return res

def mod_inv(x, mod=MOD):
    return mod_pow(x, mod - 2, mod)

def mod_div(a, b, mod=MOD):
    return (a % mod) * mod_inv(b, mod) % mod


T = int(input())
for _ in range(T):
    R, G, B, K = map(int, input().split())

    term1 = (K % MOD) * mod_div(B + G, B) % MOD   

    p = mod_div(B, B + 1)                      
    pK = mod_pow(p, K)                            
    term2 = (R % MOD) * (1 - pK) % MOD            

    res = (term1 + term2) % MOD
    print(res)
