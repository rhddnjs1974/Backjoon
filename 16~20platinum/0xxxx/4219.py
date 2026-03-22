import sys
input = sys.stdin.readline

case = 0

while True:
    case += 1
    dx, dy, n, q = map(int, input().split())
    if dx == 0 and dy == 0 and n == 0 and q == 0:
        break

    w = dx+dy+1
    d = [[0] * w for _ in range(w)]

    for _ in range(n):
        x, y = map(int, input().split())
        d[x+y][x-y+dy] += 1

    for i in range(1, w):
        s = 0
        for j in range(1, w):
            s += d[i][j]
            d[i][j] = d[i-1][j]+s

    print("Case "+str(case)+":")

    minv = 1-dy
    maxv = dx-1
    maxu = dx+dy

    for _ in range(q):
        dist = int(input())

        ans = -1
        ax = 1
        ay = 1

        for ty in range(1, dy+1):
            a = 1-ty
            b = 1+ty

            for tx in range(1, dx+1):
                l = max(a-dist, minv)
                r = min(a+dist, maxv)
                u1 = max(b-dist, 2)
                u2 = min(b+dist, maxu)

                x1 = l+dy
                x2 = r+dy
                y1 = u1
                y2 = u2

                v = d[y2][x2]-d[y1-1][x2]-d[y2][x1-1]+d[y1-1][x1-1]

                if v > ans:
                    ans = v
                    ax = tx
                    ay = ty

                a += 1
                b += 1

        print(ans,"("+str(ax)+","+str(ay)+")")
