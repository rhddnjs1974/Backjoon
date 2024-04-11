import sys
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    else:
        tree[node] = init(node * 2, start, (start + end) // 2) + init(node * 2 + 1, (start + end) // 2 + 1, end)
        return tree[node]
def subSum(node, start, end, index):

    if start==end:
        return start
    if tree[node*2]>=index:
        tree[node*2]-=1
        return subSum(node * 2, start, (start + end) // 2, index)
    else:
        tree[node*2+1]-=1
        return subSum(node * 2 + 1, (start + end) // 2 + 1, end, index-tree[node*2+1])


n,m = map(int,input().split())
l = [1]*n
tree = [0] * (300000)

ma = 100001

init(1, 0, n - 1)

now = m-1

for i in range(n):
    print(now)
    p = subSum(1, 0, n - 1, now)
    print(p+1,"p+1")
    now += m-1
    now %= tree[1]



