import sys
input = sys.stdin.readline

MOD = 10**9 + 7

N = int(input().strip())
H = list(map(int, input().split()))
H.sort()

inv = [0] * (N + 2)
inv[1] = 1
for i in range(2, N + 2):
    inv[i] = MOD - (MOD // i) * inv[MOD % i] % MOD

ans = 0
L = 0

i = 0
while i < N:
    j = i
    while j < N and H[j] == H[i]:
        j += 1
    f = j - i
    ge = N - L
    ans = (ans + f * (L % MOD) % MOD * inv[ge + 1]) % MOD
    L += f
    i = j

print(ans)
