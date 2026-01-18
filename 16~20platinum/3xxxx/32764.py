import sys
input = sys.stdin.readline

MOD = 1000000007

N, Q = map(int, input().split())
A = list(map(int, input().split()))

pref = [0] * (N + 1)
for i in range(1, N + 1):
    pref[i] = pref[i - 1] + A[i - 1]

diff = [0] * (N + 3)

for i in range(Q):
    l, r = map(int, input().split())
    S = pref[r] - pref[l - 1]
    v = pow(S, MOD - 2, MOD)
    diff[l] = (diff[l] + v) % MOD
    diff[r+1] = (diff[r+1] - v) % MOD

ans = [0] * N
cur = 0
for i in range(1, N + 1):
    cur = (cur + diff[i]) % MOD
    gi = A[i - 1] * (A[i - 1]- 1) % MOD
    ans[i-1] = gi * cur % MOD

print(*ans)
