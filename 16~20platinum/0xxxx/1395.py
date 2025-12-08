import sys
import math
input = sys.stdin.readline
"""
def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    else:
        tree[node] = init(node * 2, start, (start + end) // 2) + init(node * 2 + 1, (start + end) // 2 + 1, end)
        return tree[node]
"""

def update_lazy(node,start,end):
    lazy[node] = lazy[node]%2
    if lazy[node] == 1:
        tree[node] = (end-start+1)-tree[node]
        if start!=end:
            lazy[node*2] += 1
            lazy[node*2+1] += 1
        lazy[node] = 0

def query(node, start, end, left, right):
    update_lazy(node,start,end)
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    return query(node * 2, start, (start + end) // 2, left, right) + query(node * 2 + 1, (start + end) // 2 + 1, end,
                                                                             left, right)
def update_range(node, start, end, left, right):
    update_lazy(node,start,end)
    if left>end or right<start:
        return
    if left<=start and end<=right:
        tree[node] = (end-start+1)-tree[node]
        if start!= end:
            lazy[node*2] += 1
            lazy[node*2+1] += 1
        return

    update_range(node*2,start,(start+end)//2,left,right)
    update_range(node*2+1,(start+end)//2 +1,end,left,right)
    tree[node] = tree[node*2] + tree[node*2 +1]
    
n, m = map(int, input().split())
l = []


h = math.ceil(math.log2(n))
tree_size = 1<<(h+1)
tree = [0]*tree_size
lazy = [0]*tree_size
#init(1, 0, n - 1)

for i in range(m):
    a, *q = map(int, input().rstrip().split())

    if a == 0:
        left,right = q
        update_range(1, 0, n - 1, left-1, right-1)
    elif a == 1:
        left, right = q
        print(query(1, 0, n - 1, left - 1, right - 1))