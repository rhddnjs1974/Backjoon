def s_factorial(n):
    x = 1
    for i in range(2, n + 1):
        x *= i
    return x

def fact_mod_prime(n, p):
    if n <= 1:
        return 1
    tail_len = (p - 1) - n
    
    if n <= tail_len:
        r = 1
        for i in range(2, n + 1):
            r = (r * i) % p
        return r
    else:
        prod = 1
        for i in range(n + 1, p):
            prod = (prod * i) % p
        return (-pow(prod, p - 2, p)) % p


N, K, P = map(int,input().split())

if N == 2:
    print(2 % P)
elif N == 3:
    if K == 2:
        print(720 % P)
    elif K == 3:
        if 720 >= P:
            print(0)
        else:
            print(fact_mod_prime(720, P))
    else:
        print(0)
else:
    if K >= 3:
        print(0)
    else:
        if N >= 13:
            print(0)
        else:
            n = s_factorial(N)
            if n >= P:
                print(0)
            else:
                print(fact_mod_prime(n, P))