import sys

input = sys.stdin.readline
N = int(input())

DEN = 1000000.0

q_list = [0.0] * N

l = 0
S = 0.0
P = 1.0
best = 0.0

i = 0
while i < N:
    x = int(input())
    q = x / (DEN - x)
    q_list[i] = q

    S += q
    P *= (1.0 + q)

    val = S / P
    if val > best:
        best = val

    while S > 1.0 and l <= i:
        ql = q_list[l]
        S -= ql
        P /= (1.0 + ql)
        l += 1

        val = S / P
        if val > best:
            best = val

    i += 1

ans = int(best * 1000000.0)
print(ans)
