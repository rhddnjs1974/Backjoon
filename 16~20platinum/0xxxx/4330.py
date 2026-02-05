import sys
import math

input = sys.stdin.readline

names = [
    "N","NbE","NNE","NEbN","NE","NEbE","ENE","EbN",
    "E","EbS","ESE","SEbE","SE","SEbS","SSE","SbE",
    "S","SbW","SSW","SWbS","SW","SWbW","WSW","WbS",
    "W","WbN","WNW","NWbW","NW","NWbN","NNW","NbW"
]
angle = {}

for i in range(32):
    angle[names[i]] = i * 11.25

def dist_point_segment(px, py, ax, ay, bx, by):
    abx = bx - ax
    aby = by - ay
    apx = px - ax
    apy = py - ay
    denom = abx * abx + aby * aby
    
    if denom == 0.0:
        return math.hypot(px - ax, py - ay)
    t = (apx * abx + apy * aby) / denom
    if t < 0.0:
        t = 0.0
    elif t > 1.0:
        t = 1.0
    cx = ax + t * abx
    cy = ay + t * aby
    return math.hypot(px - cx, py - cy)

while True:
    n = int(input())
    if n == 0:
        break

    steps = []
    for _ in range(n):
        dir_name, paces_s = input().split()
        steps.append((angle[dir_name], float(paces_s)))

    d = float(input())

    xw = 0.0
    yw = 0.0
    points = [(0.0, 0.0)]
    for theta, p in steps:
        rad = math.radians(theta)
        xw += p * math.sin(rad)
        yw += p * math.cos(rad)
        points.append((xw, yw))

    xt = 0.0
    yt = 0.0
    for theta, p in steps:
        rad = math.radians(theta + d)
        xt += p * math.sin(rad)
        yt += p * math.cos(rad)

    best = 1e100
    i = 1
    while i < len(points):
        ax, ay = points[i - 1]
        bx, by = points[i]
        cur = dist_point_segment(xt, yt, ax, ay, bx, by)
        if cur < best:
            best = cur
        i += 1

    print("%.2f"%(best))
