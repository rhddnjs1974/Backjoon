import sys
input = sys.stdin.readline

def power(a,b):
    global n,p
    if b==1:
        for i in range(n):
            for j in range(n):
                a[i][j] %= p
        return a

    tmp = power(a,b//2)
    if b%2==0:
        return mat_mul(tmp,tmp)
    else:
        return mat_mul(mat_mul(tmp,tmp),a)

def mat_mul(A,B):
    global n,p
    C = [[0]*n for i in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
            C[i][j] %= p
    return C

def fib_mod(k, mod):
    global n, p
    n = 2
    p = mod
    if k == 0:
        return 0
    base = [[1, 1], [1, 0]]
    M = power(base, k)
    return M[0][1] % mod

def pisano_10_pow(m):
    if m == 1:
        return 60
    return 15 * (10 ** (m - 1))

def min_k_for_digits(n_digits):
    if n_digits <= 1:
        return 0
    threshold = 10 ** (n_digits - 1)
    a = 0
    b = 1
    k = 1
    if a >= threshold:
        return 0
    if b >= threshold:
        return 1
    while True:
        a, b = b, a + b
        k += 1
        if b >= threshold:
            return k

s = input().rstrip()
n_digits = len(s)

def target_mod(m):
    if m <= 0:
        return 0
    part = s[-m:]
    return int(part)

cands = []
P1 = 60
t1 = target_mod(1) % 10
for k in range(P1):
    if fib_mod(k, 10) == t1:
        cands.append(k)

m = 1
while m < n_digits and cands:
    Pm = pisano_10_pow(m)
    mod_next = 10 ** (m + 1)
    t_next = target_mod(m + 1) % mod_next

    if m == 1:
        mult = 5
        Pnext = 300
    else:
        mult = 10
        Pnext = Pm * 10

    nxt = []
    seen = set()
    for k0 in cands:
        for add in range(mult):
            k = k0 + add * Pm
            if fib_mod(k, mod_next) == t_next:
                kk = k % Pnext
                if kk not in seen:
                    seen.add(kk)
                    nxt.append(kk)
    cands = nxt
    m += 1

if not cands:
    print("NIE")
else:
    min_k = min_k_for_digits(n_digits)

    ans = None
    for k in cands:
        if k >= min_k:
            ans = k
            break
    if ans is None:
        print("NIE")
    else:
        print(ans)
