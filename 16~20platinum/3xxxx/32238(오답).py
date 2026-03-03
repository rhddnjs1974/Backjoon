# 오답


import sys
input = sys.stdin.readline

pd = [0.0] * 10
for i in range(1, 10):
    p, q = map(int, input().split())
    pd[i] = q / (p + q)

x, y = map(int, input().split())
rb = x / (x + y)
sb = y / (x + y)

n = int(input())
s = input().strip()

pi = [0] * n
j = 0
for i in range(1, n):
    while j > 0 and s[i] != s[j]:
        j = pi[j - 1]
    if s[i] == s[j]:
        j += 1
    pi[i] = j

dd = [[0] * 10 for _ in range(n + 1)]
for i in range(n + 1):
    for d in range(10):
        if i < n and ord(s[i]) - 48 == d:
            dd[i][d] = i + 1
        else:
            if i == 0:
                dd[i][d] = 0
            else:
                dd[i][d] = dd[pi[i - 1]][d]

pp = [0] * (n + 1)
for i in range(1, n + 1):
    pp[i] = pi[i - 1]

f = [0] * (n + 1)

for _ in range(200):
    nf = f[:]
    for k in range(n):
        best = 1e100

        j1 = dd[k][0]
        v = 1 + f[j1]
        if v < best:
            best = v

        for d in range(1, 10):
            q = pd[d]
            p = 1 - q

            a1 = dd[k][d]
            a2 = dd[a1][d]

            forward = p * f[a1] + q * f[a2]

            b1 = pp[a1]

            if b1 > 0:
                b2 = pp[b1]
            else:
                b2 = 0

            if b2 > 0:
                b3 = pp[b2]
            else:
                b3 = 0

            back = p * (rb * f[b1] + sb * f[b2]) + q * (rb * f[b2] + sb * f[b3])

            if forward < back:
                v = 1 + forward
            else:
                v = 1 + back

            if v < best:
                best = v

        nf[k] = best
    f = nf

ans = f[0]

if ans > 1e90:
    print(-1)
else:
    print(ans)