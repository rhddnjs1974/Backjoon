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


T = int(input())

for _ in range(T):
    n = int(input())
    arr = []
    arr2 = []
    for i in range(n):
        x,y = map(int,input().split())
        arr.append([-x,0])
        arr2.append((y,-x,i))

    arr2.sort()
    for j in range(n):
        arr[arr2[j][2]][1] = j+1


    l = []
    tree = [0] * (263000)

    arr.sort()
    ans = 0
    for a,b in arr:
        ans += subSum(1, 0, n - 1, 0, b)
        update(1, 0, n - 1, b)

    print(ans)