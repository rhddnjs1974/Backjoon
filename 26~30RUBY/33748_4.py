import sys
import math

XMIN, XMAX = -1000, 1000
YMIN, YMAX = -1000, 1000
BAND_W = 47

def build_lengths(limit_i=78, limit_j=25):
    seen = set()
    items = []
    for i in range(limit_i):
        for j in range(1, limit_j):
            h2 = i*i + j*j
            if h2 == 0 or h2 in seen:
                continue
            seen.add(h2)
            dx = min(i, j)
            dy = max(i, j)
            L = math.sqrt(h2)
            items.append((L, dx, dy))
    items.sort(reverse=True, key=lambda t: t[0])
    return items

def sqd(a,b): return (a[0]-b[0])**2 + (a[1]-b[1])**2

def nearest_unique(P, i):
    best = None; bd=None
    for j in range(len(P)):
        if j == i: continue
        d = sqd(P[i], P[j])
        if bd is None or d < bd: best=j; bd=d
        elif d == bd: return None, None
    return best, bd


def choose_sx_in_band(x, dx, Lleft):
    if Lleft <= x + dx <= Lleft + BAND_W: return +1
    if Lleft <= x - dx <= Lleft + BAND_W: return -1
    mid = Lleft + BAND_W/2
    return +1 if abs((x+dx)-mid) < abs((x-dx)-mid) else -1

def generate(n):
    need = n - 1
    items = build_lengths(78, 37)
    if need > len(items):
        raise ValueError("길이 후보가 부족합니다. limit_i/j를 늘리세요.")

    avail_end = 0  

    P = []
    x, y = -1000, -1000
    P.append((x,y))

    Lleft = min(max(XMIN, x), XMAX - BAND_W)

    vdir = +1

    used = 0
    last_len = float('inf')  

    idx = 0

    mode = "VERT" 
    while used < need:
        if mode == "VERT":
            found = False
            while idx < len(items):
                L, dx, dy = items[idx]
                if L >= last_len:
                    idx += 1
                    continue

                ny = y + vdir*dy
                if ny < YMIN or ny > YMAX:

                    mode = "HORIZ_PENDING"
                    found = False
                    break

                sx = choose_sx_in_band(x, dx, Lleft)
                nx = x + sx*dx

                if not (Lleft <= nx <= Lleft + BAND_W):
                    sx = -sx
                    nx = x + sx*dx
                    if not (Lleft <= nx <= Lleft + BAND_W):
                        idx += 1
                        continue

                x, y = nx, ny
                P.append((x,y))
                used += 1
                last_len = L
                idx += 1
                found = True
                break

            if mode == "HORIZ_PENDING":

                continue

            if not found and mode == "VERT":

                mode = "HORIZ_PENDING"
                continue

        if mode == "HORIZ_PENDING":

            h_found = False

            h_idx = idx
            best_h = None
            while h_idx < len(items):
                Lh, dxh, dyh = items[h_idx]
                if Lh >= last_len: 
                    h_idx += 1
                    continue
                H = math.floor(Lh)
                if H <= 0:
                    h_idx += 1
                    continue

                if x + H <= XMAX - BAND_W:
                    best_h = (h_idx, Lh, H)
                    break

                h_idx += 1

            if best_h is None:
                raise RuntimeError("가로 전환을 위한 유효한 H를 찾지 못했습니다. (박스 오른쪽 끝)")

            _, Lh, H = best_h

            x = x + H 


            P.append((x, y))
            used += 1


            Lleft = x 
            last_len = H

            vdir *= -1

            mode = "VERT"

    return P

n = int(input())
pts = generate(n)

for x,y in pts:
    print(x, y)

