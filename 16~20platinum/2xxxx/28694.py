import sys
input = sys.stdin.readline

MOD = 10**9 + 7
INV2 = (MOD + 1) // 2 
INV4 = (INV2 * INV2) % MOD

T = int(input())
for i in range(T):
    n, m = map(int, input().split())
    print((n % MOD) * INV2 % MOD, (n % MOD) * INV4 % MOD)
