import sys
input = sys.stdin.readline

n, r, m = map(int, input().split())

T = [0] * (m + 2)
P = [0.0] * (m + 2)
D = [0] * (m + 2)

for i in range(1, m + 1):
    t, p, d = input().split()
    T[i] = int(t)
    P[i] = float(p)
    D[i] = int(d)

T[m + 1] = n
P[m + 1] = 1.0
D[m + 1] = 0

seg = [0] * (m + 2)
for i in range(1, m + 1):
    seg[i] = T[i + 1] - T[i]

t1 = T[1]

def start_value(X):
    dp_next = [0.0] * r

    for i in range(m, 0, -1):
        p = P[i]
        q = 1.0 - p
        d = D[i]
        dt = seg[i]

        dp_cur = [0.0] * r
        for s in range(r):
            best = X

            s_succ = s + dt
            succ_future = X
            if s_succ < r:
                succ_future = dp_next[s_succ]
            succ_cost = dt + succ_future

            fail_cost = X

            s_fail = s + d + dt
            cont_future = X
            if s_fail < r:
                cont_future = dp_next[s_fail]
            cont_cost = d + dt + cont_future

            if cont_cost < fail_cost:
                fail_cost = cont_cost

            attempt = p * succ_cost + q * fail_cost
            if attempt < best:
                best = attempt

            dp_cur[s] = best

        dp_next = dp_cur

    return t1 + dp_next[t1]

lo = 0.0
hi = 1.0
for _ in range(300):
    v = start_value(hi)
    if v < hi:
        break
    hi *= 2.0

for _ in range(80):
    mid = (lo + hi) * 0.5
    v = start_value(mid)
    if v < mid:
        hi = mid
    else:
        lo = mid

ans = (lo + hi) * 0.5
print(ans)
