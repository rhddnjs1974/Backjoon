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

n = int(input())
l = []
tree = [0] * (300000)

arr = [0]+list(map(int,input().split()))

for i in range(1,n+1):
    t = arr[i]-arr[i-1]
    l.append(t)

m = int(input())

init(1, 0, n - 1)


for i in range(m):
    a = list(map(int, input().rstrip().split()))

    if a[0] == 1:
        i = a[1]
        j = a[2]
        k = a[3]
        update(1, 0, n - 1, i-1, k)
        update(1, 0, n - 1, j, -k)

    elif a[0] == 2:
        x = a[1]
        print(subSum(1, 0, n - 1, 0, x - 1))

