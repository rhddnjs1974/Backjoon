import sys
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree1[node] = l[start]
        return tree1[node]
    else:
        a = init(node * 2, start, (start + end) // 2)
        b = init(node * 2 + 1, (start + end) // 2 + 1, end)
        tree1[node] = min(a,b)

        return tree1[node]

def subSum(node, start, end, left, right):
    if left > end or right < start:
        return 1e10
    if left <= start and end <= right:
        return tree1[node]
    a = subSum(node * 2, start, (start + end) // 2, left, right)
    b = subSum(node * 2 + 1, (start + end) // 2 + 1, end, left, right)

    return min(a,b)

n, m = map(int, input().split())
l = []
tree1 = [0] * (400000) #min

for i in range(n):
    l.append(int(input()))

init(1, 0, n - 1)

for i in range(m):
    a, b = map(int, input().rstrip().split())

    print(subSum(1, 0, n - 1, a - 1, b - 1))
