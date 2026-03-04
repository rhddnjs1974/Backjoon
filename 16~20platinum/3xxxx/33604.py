import sys
input = sys.stdin.readline

def pick(ax, ay, bx, by, D, E):
    du = (bx+by)-(ax+ay)
    dv = (bx-by)-(ax-ay)

    for uf in (D, -D):
        if abs(uf-du) > E:
            continue
        lo = dv-E
        hi = dv+E
        if lo < -D:
            lo = -D
        if hi > D:
            hi = D
        if lo > hi:
            continue

        if abs(uf-du) == E:
            if (lo & 1) != (uf & 1):
                lo += 1
            if lo <= hi:
                uu = (ax+ay)+uf
                vv = (ax-ay)+lo
                return ((uu+vv)//2, (uu-vv)//2)
        else:
            for vc in (dv+E, dv-E):
                if vc < lo or vc > hi:
                    continue
                if ((vc ^ uf) & 1) != 0:
                    continue
                uu = (ax+ay)+uf
                vv = (ax-ay)+vc
                return ((uu+vv)//2, (uu-vv)//2)

    for vf in (D, -D):
        if abs(vf-dv) > E:
            continue
        lo = du-E
        hi = du+E
        if lo < -D:
            lo = -D
        if hi > D:
            hi = D
        if lo > hi:
            continue

        if abs(vf-dv) == E:
            if (lo & 1) != (vf & 1):
                lo += 1
            if lo <= hi:
                uu = (ax+ay)+lo
                vv = (ax-ay)+vf
                return ((uu+vv)//2, (uu-vv)//2)
        else:
            for uc in (du+E, du-E):
                if uc < lo or uc > hi:
                    continue
                if ((uc ^ vf) & 1) != 0:
                    continue
                uu = (ax+ay)+uc
                vv = (ax-ay)+vf
                return ((uu+vv)//2, (uu-vv)//2)

    return None

n = int(input())
a, b = map(int, input().split())
d = list(map(int, input().split()))

d0 = abs(a)+abs(b)
S = d0
for i in range(n-1):
    S += d[i]

if (S & 1) != 0:
    print("NO")
    exit()

if d0 > S-d0:
    print("NO")
    exit()

for i in range(n-1):
    if d[i] > S-d[i]:
        print("NO")
        exit()

ANS = [(a, b)]

for m in range(n,2,-1):
    sm = 0
    for i in range(m-2):
        sm += d[i]

    DD = min(d0+d[m-2],sm)

    p = pick(0, 0, ANS[-1][0], ANS[-1][1], DD, d[m-2])
    if p is None:
        print("NO")
        exit()

    ANS.append(p)
    d0 = DD


ANS.append((0, 0))
ANS.reverse()

print("YES")
for x, y in ANS:
    print(x, y)