import sys
input = sys.stdin.readline

MOD = 998244353

n = int(input())
arr = list(map(int, input().split()))

m = 0
for i in range(n):
    m += arr[i]
m %= MOD

inv4 = pow(4, MOD-2, MOD)
inv12 = pow(12, MOD-2, MOD)

pref = 0
M = 0
Ohh = 0
Oll = 0
Och = 0

for i in range(n):
    ai = arr[i]

    L = pref
    G = m - pref - ai
    G %= MOD

    M += ai * L
    M %= MOD

    Ohh += ai * L * (L - 1)
    Ohh %= MOD

    Oll += ai * G * (G - 1)
    Oll %= MOD

    Och += 2 * ai * L * G
    Och %= MOD

    pref += ai
    pref %= MOD

ans = 0

temp = M * M
temp %= MOD
temp += M
temp %= MOD
temp *= inv4
temp %= MOD

ans += temp
ans %= MOD

adjust = Ohh + Oll - Och
adjust %= MOD
adjust *= inv12
adjust %= MOD

ans += adjust
ans %= MOD

print(ans)