import sys
input = sys.stdin.readline

def ccw(x1,y1,x2,y2,x3,y3):
    c = (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
    return c

def convex_hull(position):
    convex = []
    for p3 in position:
        while len(convex)>=2:
            p1,p2 = convex[-2],convex[-1]
            if ccw(*p1,*p2,*p3)>0:
                break
            convex.pop()
        convex.append(p3)
    return convex

def on_segment(a, b, p):
    if ccw(a[0], a[1], b[0], b[1], p[0], p[1]) != 0:
        return False
    if a[0] <= b[0]:
        if p[0] < a[0] or p[0] > b[0]:
            return False
    else:
        if p[0] < b[0] or p[0] > a[0]:
            return False
    if a[1] <= b[1]:
        if p[1] < a[1] or p[1] > b[1]:
            return False
    else:
        if p[1] < b[1] or p[1] > a[1]:
            return False
    return True

def build_hull_polygon(pts):
    x = convex_hull(pts)
    pts.reverse()
    y = convex_hull(pts)
    pts.reverse()

    if len(x) + len(y) - 2 < 3:
        return []

    return x + y[1:-1]

while True:
    line = input().strip()
    if not line:
        break
    n = int(line)
    if n == 0:
        break

    pts = []
    for _ in range(n):
        a, b = map(int, input().split())
        pts.append((a, b))

    layers = 0
    while len(pts) >= 3:
        pts.sort()
        poly = build_hull_polygon(pts)
        if len(poly) < 3:
            break

        m = len(poly)

        new_pts = []
        for p in pts:
            on_bd = False
            i = 0
            while i < m:
                a = poly[i]
                b = poly[0] if i + 1 == m else poly[i+1]
                if on_segment(a, b, p):
                    on_bd = True
                    break
                i += 1
            if not on_bd:
                new_pts.append(p)

        if len(new_pts) == len(pts):
            break

        pts = new_pts
        layers += 1

    if layers % 2 == 1:
        print("Take this onion to the lab!")
    else:
        print("Do not take this onion to the lab!")
