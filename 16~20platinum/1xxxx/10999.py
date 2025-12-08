import sys
import math
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    else:
        tree[node] = init(node * 2, start, (start + end) // 2) + init(node * 2 + 1, (start + end) // 2 + 1, end)
        return tree[node]

def update_lazy(node,start,end):
    if lazy[node] != 0:
        tree[node] += (end-start+1)*lazy[node]
        if start!=end:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0

def query(node, start, end, left, right):
    update_lazy(node,start,end)
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    return query(node * 2, start, (start + end) // 2, left, right) + query(node * 2 + 1, (start + end) // 2 + 1, end,
                                                                             left, right)
def update_range(node, start, end, left, right, diff):
    update_lazy(node,start,end)
    if left>end or right<start:
        return
    if left<=start and end<=right:
        tree[node] += (end-start+1)*diff
        if start!= end:
            lazy[node*2] += diff
            lazy[node*2+1] += diff
        return
    tree[node] += diff
    update_range(node*2,start,(start+end)//2,left,right,diff)
    update_range(node*2+1,(start+end)//2 +1,end,left,right,diff)
    tree[node] = tree[node*2] + tree[node*2 +1]
n, m, k = map(int, input().split())
l = []

for i in range(n):
    l.append(int(input()))

h = math.ceil(math.log2(n))
tree_size = 1<<(h+1)
tree = [0]*tree_size
lazy = [0]*tree_size
init(1, 0, n - 1)

for i in range(m + k):
    a, *q = map(int, input().rstrip().split())

    if a == 1:
        left,right,diff = q
        update_range(1, 0, n - 1, left-1, right-1, diff)
    elif a == 2:
        left, right = q
        print(query(1, 0, n - 1, left - 1, right - 1))