import sys
from itertools import permutations
input = sys.stdin.readline

MOD = 998244353

N, M = map(int, input().split())

arr = [0] * (N + 1)
for _ in range(M):
    t, i = map(int, input().split())
    arr[i] = t

if M == 0:
    facto = 1
    for i in range(2,N+1):
        facto = (facto*i) % MOD

    H = 0
    for i in range(1,N+1):
        H = (H + pow(i, MOD-2, MOD)) % MOD

    inv4 = pow(4, MOD-2, MOD)
    inv12 = pow(12, MOD-2, MOD)

    term1 = N * (N-1) % MOD
    term1 = term1 * inv4 % MOD
    term1 = term1 * ((N-H) % MOD) % MOD

    term2 = (2*N-1) % MOD
    term2 = term2*inv12 % MOD

    ans = facto*((term1+term2) % MOD) % MOD
    print(ans)
else:
    ans = 0
    for p in permutations(range(1, N + 1)):
        flag = 1
        for i in range(1, N + 1):
            x = p[i-1]
            a = arr[i]
            if a == 1:
                if x <= i:
                    flag = 0
                    break
            elif a == 2:
                if x >= i:
                    flag = 0
                    break
        if flag == 0:
            continue

        inv = 0
        for i in range(N):
            for j in range(i + 1, N):
                if p[i] > p[j]:
                    inv += 1

        visit = [0] * (N+1)
        cycles = 0
        for i in range(1,N+1):
            if visit[i]==0:
                cycles += 1
                c = i
                while visit[c]==0:
                    visit[c] = 1
                    c = p[c-1]

        g = N - cycles
        ans = (ans + inv*g) % MOD

    print(ans)
