import sys
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        full[node] = y[start+1]-y[start]
        tree[node] = 0
        return
    mid = (start+end)//2
    init(node*2, start, mid)
    init(node*2+1, mid+1, end)
    full[node] = full[node*2]+full[node*2+1]
    tree[node] = 0

def update_lazy(node,start,end):
    if lazy[node] != 0:
        tree[node] = full[node]-tree[node]
        if start!=end:
            lazy[node*2] ^= 1
            lazy[node*2+1] ^= 1
        lazy[node] = 0

def query(node, start, end, left, right):
    update_lazy(node,start,end)
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    return query(node * 2, start, (start + end) // 2, left, right) + query(node * 2 + 1, (start + end) // 2 + 1, end, left, right)

def update_range(node, start, end, left, right, diff):
    update_lazy(node,start,end)
    if left>end or right<start:
        return
    if left<=start and end<=right:
        lazy[node] ^= 1
        update_lazy(node,start,end)
        return

    update_range(node*2,start,(start+end)//2,left,right,diff)
    update_range(node*2+1,(start+end)//2 +1,end,left,right,diff)
    tree[node] = tree[node*2] + tree[node*2 +1]

n = int(input())
e = []
y = []

for i in range(n):
    x1,y1,x2,y2 = map(int, input().split())
    e.append((x1,y1,y2))
    e.append((x2,y1,y2))
    y.append(y1)
    y.append(y2)

y = list(set(y))
y.sort()

m = len(y)-1
if m == 0:
    print(0)
    exit()

d = {}
for i in range(len(y)):
    d[y[i]] = i

tree = [0 for i in range(4*m+5)]
lazy = [0 for i in range(4*m+5)]
full = [0 for i in range(4*m+5)]

init(1, 0, m-1)

e.sort()

ans = 0
i = 0
px = e[0][0]

while i < (2*n):
    x = e[i][0]
    ans += tree[1] * (x-px)

    while i < (2*n) and e[i][0] == x:
        l = d[e[i][1]]
        r = d[e[i][2]]-1
        if l <= r:
            update_range(1, 0, m-1, l, r, 1)
        i += 1

    px = x

print(ans)