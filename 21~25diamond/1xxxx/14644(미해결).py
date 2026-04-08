import sys
input = sys.stdin.readline

def update(i, v):
    while i <= m:
        tree[i] += v
        i += i & (-i)

def query(i):
    s = 0
    while i > 0:
        s += tree[i]
        i -= i & (-i)
    return s

def kth(k):
    pos = 0
    for i in range(LOG-1, -1, -1):
        nxt = pos+(1 << i)
        if nxt <= m and tree[nxt] < k:
            k -= tree[nxt]
            pos = nxt
    return pos+1

n = int(input())
pr = [0] * n
pc = [0] * n
for i in range(n):
    pr[i], pc[i] = map(int, input().split())
yr = [0] * n
yc = [0] * n
for i in range(n):
    yr[i], yc[i] = map(int, input().split())

vals = list(set(pr+yr))
vals.sort()
comp = {}
for i in range(len(vals)):
    comp[vals[i]] = i+1
m = len(vals)

tree = [0] * (m+1)
LOG = m.bit_length()+1

events = []
for i in range(n):
    events.append((pc[i], 1, pr[i], i))
for i in range(n):
    events.append((yc[i], 0, yr[i], i))
events.sort()

ans = [-1] * n
who = {}
ok = True

for c, t, r, idx in events:
    if not ok:
        break
    ci = comp[r]
    if t == 1:
        if query(ci)-query(ci-1) > 0:
            ok = False
            break
        update(ci, 1)
        who[ci] = idx
    else:
        k = query(ci-1)
        if k == 0:
            ok = False
            break
        p = kth(k)
        update(p, -1)
        pidx = who.pop(p)
        ans[pidx] = idx

if ok and who:
    ok = False

rects = [None] * n
if ok:
    for i in range(n):
        r1, c1, r2, c2 = pr[i], pc[i], yr[ans[i]], yc[ans[i]]
        if r1 >= r2 or c1 >= c2:
            ok = False
            break
        rects[i] = (r1, c1, r2, c2)

if ok:
    order = [(rects[i][0], -rects[i][2], i) for i in range(n)]
    order.sort()
    lst = []
    for _, _, i in order:
        r1, c1, r2, c2 = rects[i]
        while lst and rects[lst[-1]][2] < r1:
            lst.pop()
        j = len(lst)-1
        while j >= 0:
            tr1, tc1, tr2, tc2 = rects[lst[j]]
            if tr2 < r1:
                j -= 1
                continue
            cd = tc2 < c1 or c2 < tc1
            if tr1 < r1 and r2 < tr2:
                if tc1 < c1 and c2 < tc2:
                    break
                elif cd:
                    j -= 1
                    continue
                else:
                    ok = False
                    break
            elif tr2 < r2:
                if cd:
                    j -= 1
                    continue
                else:
                    ok = False
                    break
            else:
                if cd:
                    j -= 1
                    continue
                else:
                    ok = False
                    break
        if not ok:
            break
        lst.append(i)

if not ok:
    print("syntax error")
else:
    for i in range(n):
        print(ans[i]+1)
