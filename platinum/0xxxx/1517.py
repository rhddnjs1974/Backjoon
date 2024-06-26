import sys
input = sys.stdin.readline

def subSum(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    return subSum(node * 2, start, (start + end) // 2, left, right) + subSum(node * 2 + 1, (start + end) // 2 + 1, end,
                                                                             left, right)
def update(node, start, end, index):
    if index < start or index > end:
        return
    tree[node] += 1
    if start != end:
        update(node * 2, start, (start + end) // 2, index)
        update(node * 2 + 1, (start + end) // 2 + 1, end, index)

n = int(input())
arr = list(map(int,input().split()))

tree = [0] * (3000000)

l = []
for i in range(n):
    l.append((arr[i],i))

l.sort()
ans = 0

for i in range(n):
    a = l[i][1]

    ans += subSum(1,0,n-1,a,n-1)
    update(1, 0, n - 1, a-1)

print(ans)