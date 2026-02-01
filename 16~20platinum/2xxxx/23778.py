import math

n, i, k = map(int, input().split())

cn = (n + 1) / 2.0

c = [0.0] * (n - 1)

S = 0.0
for t in range(n, 1, -1):
    ct1 = (cn + S - t) / (t - 1)
    c[t - 2] = ct1
    S += ct1

nf = float(n)

tail = 0.0
for r in range(i, n):
    tail += c[r - 1] * math.pow(r / nf, k)

ad = 0.0
if i > 1:
    r = i - 1
    ad = c[r - 1] * math.pow(r / nf, k) * (-r)

ans = cn + tail + ad
print(ans)
