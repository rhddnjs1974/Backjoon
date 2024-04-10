import sys
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree1[node] = l[start]
        tree2[node] = l[start]
        return tree1[node],tree2[node]
    else:
        a = init(node * 2, start, (start + end) // 2)
        b = init(node * 2 + 1, (start + end) // 2 + 1, end)
        tree1[node] = min(a[0],b[0])
        tree2[node] = max(a[1],b[1])
        return tree1[node],tree2[node]

def subSum(node, start, end, left, right):
    if left > end or right < start:
        return 1e9,0
    if left <= start and end <= right:
        return tree1[node],tree2[node]
    a = subSum(node * 2, start, (start + end) // 2, left, right)
    b = subSum(node * 2 + 1, (start + end) // 2 + 1, end, left, right)

    return min(a[0],b[0]),max(a[1],b[1])

n, m = map(int, input().split())
l = []
tree1 = [0] * (300000) #min
tree2 = [0] * (300000) #max

for i in range(n):
    l.append(int(input()))

init(1, 0, n - 1)

for i in range(m):
    a, b = map(int, input().rstrip().split())

    print(*subSum(1, 0, n - 1, a - 1, b - 1))
