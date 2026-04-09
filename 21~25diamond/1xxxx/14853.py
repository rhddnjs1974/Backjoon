import sys
import math

input = sys.stdin.readline

MAXN = 3000
logfac = [0.0] * (MAXN + 1)
for i in range(2, MAXN + 1):
    logfac[i] = logfac[i - 1] + math.log(i)

def log_beta(x, y):
    return logfac[x - 1] + logfac[y - 1] - logfac[x + y - 1]

T = int(input().strip())
for _ in range(T):
    n1, m1, n2, m2 = map(int, input().split())

    a = m1 + 1
    b = n1 - m1 + 1
    c = m2 + 1
    d = n2 - m2 + 1

    logB_cd = log_beta(c, d)

    s = 0.0
    for i in range(a):
        log_term = log_beta(c + i, b + d) - math.log(b + i) - log_beta(i + 1, b) - logB_cd
        s += math.exp(log_term)

    ans = 1.0 - s
    if ans < 0.0:
        ans = 0.0
    elif ans > 1.0:
        ans = 1.0

    print(ans)
