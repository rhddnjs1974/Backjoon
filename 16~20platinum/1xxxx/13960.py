import math

N, D, C = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

setA = set(A)
setB = set(B)

t = len(setA & setB)
x0 = t
y0 = C - t
z0 = C - t

den = math.comb(N, D)

dp = [[[0.0 for _ in range(11)] for _ in range(11)] for _ in range(11)]

for total in range(0, 31):
    for x in range(0, 11):
        for y in range(0, 11):
            z = total - x - y
            if z < 0 or z > 10:
                continue

            if x + y == 0 or x + z == 0:
                dp[x][y][z] = 0.0
                continue

            r = N - (x + y + z)

            if r >= D:
                p0 = math.comb(r, D) / den
            else:
                p0 = 0.0

            acc = 0.0

            k_max = min(D, x)
            for k in range(0, k_max + 1):
                p_max = min(D - k, y)
                for p in range(0, p_max + 1):
                    q_max = min(D - k - p, z)
                    for q in range(0, q_max + 1):
                        if k == 0 and p == 0 and q == 0:
                            continue
                        rest = D - k - p - q
                        if rest < 0 or rest > r:
                            continue

                        ways = math.comb(x, k) * math.comb(y, p) * math.comb(z, q) * math.comb(r, rest)
                        prob = ways / den
                        acc += prob * dp[x - k][y - p][z - q]

            dp[x][y][z] = (1.0 + acc) / (1.0 - p0)

ans = dp[x0][y0][z0]
print(ans)
