import sys
input = sys.stdin.readline
mod = 1000000007

def get(l, r):
    if l > r:
        return 1
    if l < 0 or r >= n:
        return 0
    return dp[l][r]

def ok(i, c):
    return S[i] == c or S[i] == '?'

for _ in range(int(input())):
    n = int(input().strip())
    S = input().strip()
    if n % 3 != 0:
        print(0)
        continue

    dp = [[0] * n for _ in range(n)]
    w  = [[0] * n for _ in range(n)]

    for L in range(3, n + 1, 3):
        for l in range(0, n - L + 1):
            r = l + L - 1

            t = 0
            if ok(l, 'H') and ok(r, 'H'):
                i = l + 1
                while i <= r - 1:
                    if ok(i, 'Y'):
                        t += get(l + 1, i - 1) * get(i + 1, r - 1)
                        if t >= 8 * mod:
                            t %= mod
                    i += 3
            w[l][r] = t % mod

            now = 0
            k = l + 2
            while k <= r:
                left = w[l][k]
                right = get(k + 1, r) if k + 1 <= r else 1
                now += left * right
                k += 3
            dp[l][r] = now % mod

    print(dp[0][n - 1])
