import math

k, r = map(int, input().split())
n = 1 << k

def logC(a, b):
    return math.lgamma(a + 1) - math.lgamma(b + 1) - math.lgamma(a - b + 1)

ans = 0.0

for i in range(1, k + 1):
    m = (1 << i) - 1
    a = n - r

    if a < m:
        si = 0.0
    else:
        log_si = logC(a, m) - logC(n - 1, m)
        si = math.exp(log_si)

    ans += si

print("%.5f"%(ans))
