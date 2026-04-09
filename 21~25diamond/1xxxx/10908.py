import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
########################################

def power(a,b):
    global n,p
    if b == 0:
        I = [[0] * n for _ in range(n)]
        for i in range(n):
            I[i][i] = 1
        return I
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

########################################
MOD = 1000000007

def fib_pair(x):
    if x == 0:
        return 0, 1
    a, b = fib_pair(x // 2)
    t = (2 * b - a) % MOD
    c = (a * t) % MOD
    d = (a * a + b * b) % MOD
    if x % 2 == 0:
        return c, d
    else:
        return d, (c + d) % MOD

Nexp, K = map(int, input().split())

Fk, Fk1 = fib_pair(K)
Lk = (2 * Fk1 - Fk) % MOD

if K % 2 == 0:
    s = 1
else:
    s = MOD - 1

n = 2
p = MOD

T = [
    [Lk, 1],
    [(MOD - s) % MOD, 0]
]

P = power(T, Nexp)

A = P[0][1] % MOD
B = P[1][1] % MOD

print(A, B)