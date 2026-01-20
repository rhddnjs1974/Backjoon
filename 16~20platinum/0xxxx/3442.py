import sys
input = sys.stdin.readline

def signed_area(poly):
    s = 0
    n = len(poly)
    i = 0
    while i < n:
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        s += x1 * y2 - x2 * y1
        i += 1
    return s 

def add_group(dic, key, item):
    if key in dic:
        dic[key].append(item)
    else:
        dic[key] = [item]

def connect_pairs(adj, groups):
    for key in groups:
        lst = groups[key]
        lst.sort()
        i = 0
        while i < len(lst):
            a = lst[i][1]
            b = lst[i + 1][1]
            adj[a].append(b)
            adj[b].append(a)
            i += 2

def traverse(adj, start, second):
    order = [start, second]
    prev = start
    cur = second
    while True:
        a = adj[cur][0]
        b = adj[cur][1]
        if a != prev:
            nxt = a
        else:
            nxt = b

        if nxt == start:
            break

        order.append(nxt)
        prev = cur
        cur = nxt
    return order

while True:
    line = input()
    if not line:
        break
    line = line.strip()
    if line == "":
        continue

    N = int(line)
    if N == 0:
        break

    pts = []
    for _ in range(N):
        x, y = map(int, input().split())
        pts.append((x, y))

    start = pts[0]

    adj = {}
    for p in pts:
        adj[p] = []

    byx = {}
    byy = {}
    for x, y in pts:
        add_group(byx, x, (y, (x, y))) 
        add_group(byy, y, (x, (x, y)))

    connect_pairs(adj, byx)
    connect_pairs(adj, byy)

    n0 = adj[start][0]
    n1 = adj[start][1]

    order1 = traverse(adj, start, n0)
    order2 = traverse(adj, start, n1)

    if signed_area(order1) < 0:
        order = order1
    else:
        order = order2

    n = len(order)
    i = 0
    while i < n:
        x1, y1 = order[i]
        x2, y2 = order[(i + 1) % n]
        if x1 == x2:
            if y2 > y1:
                print("N", end="")
            else:
                print("S", end="")
        else:
            if x2 > x1:
                print("E", end="")
            else:
                print("W", end="")
        i += 1
    print()
