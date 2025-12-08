import sys
input = sys.stdin.readline


def subSum(node, start, end, index):

    if start==end:
        return start
    if tree[node*2]>=index:
        tree[node*2]-=1
        return subSum(node * 2, start, (start + end) // 2, index)
    else:
        tree[node*2+1]-=1
        return subSum(node * 2 + 1, (start + end) // 2 + 1, end, index-tree[node*2])
def update(node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff
    if start != end:
        update(node * 2, start, (start + end) // 2, index, diff)
        update(node * 2 + 1, (start + end) // 2 + 1, end, index, diff)

n = int(input())
l = []
tree = [0] * (3000000)

ma = 1000001


num = 0

for i in range(n):
    t = list(map(int, input().rstrip().split()))

    if t[0] == 2:
        x = t[1]
        diff = t[2]
        update(1, 0, ma - 1, x-1, diff)
        num+=diff
    elif t[0] == 1:
        x = t[1]
        p = subSum(1, 0, ma - 1, x)
        print(p+1)
        num-=1


