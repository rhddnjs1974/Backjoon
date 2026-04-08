import sys
input = sys.stdin.readline

n = int(input())
w = [None] * n
adj = [[] for _ in range(100)]
ind = [0] * 100
oud = [0] * 100
pa = list(range(100))

def find(x):
    while pa[x] != x:
        pa[x] = pa[pa[x]]
        x = pa[x]
    return x

for i in range(n):
    s = input()
    w[i] = s[:10]
    u = int(s[:2])
    v = int(s[8:10])
    adj[u].append((v, i))
    oud[u] += 1
    ind[v] += 1
    pu, pv = find(u), find(v)
    if pu != pv:
        pa[pu] = pv

ok = True
root = -1
for i in range(100):
    if ind[i]+oud[i] > 0:
        r = find(i)
        if root == -1:
            root = r
        elif r != root:
            ok = False
            break

start = -1
ed = -1
if ok:
    for i in range(100):
        d = oud[i]-ind[i]
        if d == 1:
            if start != -1:
                ok = False
                break
            start = i
        elif d == -1:
            if ed != -1:
                ok = False
                break
            ed = i
        elif d != 0:
            ok = False
            break

if ok and (start == -1) != (ed == -1):
    ok = False

if ok and start == -1:
    start = int(w[0][:2])

if not ok:
    print("impossible")
else:
    ptr = [0] * 100
    stk = [(start, -1)]
    res = []
    while stk:
        u = stk[-1][0]
        if ptr[u] < len(adj[u]):
            v, idx = adj[u][ptr[u]]
            ptr[u] += 1
            stk.append((v, idx))
        else:
            _, eidx = stk.pop()
            if eidx != -1:
                res.append(eidx)
    res.reverse()
    if len(res) != n:
        print("impossible")
    else:
        for i in res:
            print(w[i])
