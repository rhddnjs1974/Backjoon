import sys
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    else:
        tree[node] = init(node * 2, start, (start + end) // 2) + init(node * 2 + 1, (start + end) // 2 + 1, end)
        return tree[node]

def subSum(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    return subSum(node * 2, start, (start + end) // 2, left, right) + subSum(node * 2 + 1, (start + end) // 2 + 1, end,
                                                                             left, right)
def update(node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff
    if start != end:
        update(node * 2, start, (start + end) // 2, index, diff)
        update(node * 2 + 1, (start + end) // 2 + 1, end, index, diff)

n,q = map(int, input().split())
l = []
tree = [0] * (400000)

l = list(map(int,input().split()))

init(1, 0, n - 1)

for i in range(q):
    a, b, c,d = map(int, input().rstrip().split())
    if a>b:
        a,b=b,a
    print(subSum(1, 0, n - 1, a - 1, b - 1))

    c = c - 1
    diff = d - l[c]
    l[c] = d

    update(1, 0, n - 1, c, diff)

