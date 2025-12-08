import sys
input = sys.stdin.readline

divide = 1000000007

def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    else:
        tree[node] = init(node * 2, start, (start + end) // 2) * init(node * 2 + 1, (start + end) // 2 + 1, end)
        tree[node] %= divide
        return tree[node]

def subSum(node, start, end, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[node]
    t = subSum(node * 2, start, (start + end) // 2, left, right) * subSum(node * 2 + 1, (start + end) // 2 + 1, end,
                                                                             left, right)
    t %= divide

    return t
def update(node, start, end, index, diff):
    if index < start or index > end:
        return

    if start==end:
        tree[node] = diff
    if start != end:
        update(node * 2, start, (start + end) // 2, index, diff)
        update(node * 2 + 1, (start + end) // 2 + 1, end, index, diff)
        tree[node] = tree[node*2] * tree[node*2 +1]
        tree[node]%= divide

n, m, k = map(int, input().split())
l = []
tree = [0] * (3000000)

for i in range(n):
    l.append(int(input()))

init(1, 0, n - 1)



for i in range(m + k):
    a, b, c = map(int, input().rstrip().split())

    if a == 1:
        b = b - 1

        update(1, 0, n - 1, b, c)
    elif a == 2:
        print(int(subSum(1, 0, n - 1, b - 1, c - 1)))
