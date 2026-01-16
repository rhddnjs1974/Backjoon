import sys
input = sys.stdin.readline

MOD = 998244353

N, M = map(int, input().split())
A = list(map(int, input().split()))

S = sum(A)
if S < 2 or M < 2:
    print(0)
else:
    T = 0
    for a in A:
        T = (T + a * (a - 1) // 2) % MOD

    CM = (M*(M-1)//2) % MOD
    CS = (S*(S-1)//2) % MOD
    ans = T * CM % MOD * pow(CS, MOD - 2, MOD) % MOD
    print(ans)

