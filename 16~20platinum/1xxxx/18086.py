import math

n, k = map(int, input().split())
s = list(map(float, input().split()))

log_den = math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)

w = [0] * n
for d in range(n):
    if 0 <= k - 1 <= n-d-1:
        log_num = math.lgamma(n-d-1 + 1) - math.lgamma(k) - math.lgamma(n-d-1 - (k - 1) + 1)
        w[d] = math.exp(log_num - log_den)

ans = [0] * n
for t in range(n):
    x = 0
    for d in range(n):
        i = (t - d) % n
        x += w[d] * s[i]
    ans[t] = x

print(*ans)
