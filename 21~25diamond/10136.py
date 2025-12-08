import sys
input = sys.stdin.readline

def max_cell(a, b, c, d):

    limit = min(b,d)

    a1 = a - 1
    c1 = c - 1
    ans = 1

    k = 1
    while k <= limit:

        qb = b // k
        qd = d // k
        if qb == 0 or qd == 0:
            break

        last_b = b // qb
        last_d = d // qd
        last = min(last_b,last_d)
        if last > limit:
            last = limit

        if b // last > a1 // last and d // last > c1 // last:
            ans = last

        k = last + 1

    return ans


n = int(input())

for _ in range(n):
    smin, smax, wmin, wmax = map(int, input().split())
    print(max_cell(smin, smax, wmin, wmax))

