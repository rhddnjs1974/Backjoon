import sys
input = sys.stdin.readline

def merge(a, b):
    return (a[0]+b[0], max(a[1], a[0]+b[1]), max(b[2], b[0]+a[2]), max(a[3], b[3], a[2]+b[1]))

def init(node, start, end):
    if start == end:
        tree[node] = (l[start], l[start], l[start], l[start])
        return tree[node]
    else:
        tree[node] = merge(init(node * 2, start, (start + end) // 2), init(node * 2 + 1, (start + end) // 2 + 1, end))
        return tree[node]

def subSum(node, start, end, left, right):
    if left > end or right < start:
        return (-INF, -INF, -INF, -INF)
    if left <= start and end <= right:
        return tree[node]
    return merge(subSum(node * 2, start, (start + end) // 2, left, right), subSum(node * 2 + 1, (start + end) // 2 + 1, end, left, right))

def update(node, start, end, index, diff):
    if index < start or index > end:
        return
    if start == end:
        x = tree[node][0]+diff
        tree[node] = (x, x, x, x)
        return
    update(node * 2, start, (start + end) // 2, index, diff)
    update(node * 2 + 1, (start + end) // 2 + 1, end, index, diff)
    tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

n = int(input())
l = [0]+list(map(int, input().split()))
tree = [0 for i in range(4*n)]
INF = 10**18

init(1, 1, n)

m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    print(subSum(1, 1, n, a, b)[3])