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

def update(node, start, end, index, diff):
    print(node,start,end)

    if index < start or index > end:
        return 1e9,0
    if start==end:
        tree1[node] = diff
        tree2[node] = diff

    if start != end:
        a = update(node * 2, start, (start + end) // 2, index, diff)
        b = update(node * 2 + 1, (start + end) // 2 + 1, end, index, diff)
        tree1[node] = min(a[0], b[0])
        tree2[node] = max(a[1], b[1])
    return tree1[node], tree2[node]

T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    l = []
    tree1 = [0] * (n*3) #min
    tree2 = [0] * (n*3) #max

    for i in range(n):
        l.append(i)

    init(1, 0, n - 1)

    for i in range(m):
        a, b, c = map(int, input().rstrip().split())

        if a==0:
            update(1,0,n-1,b,l[c])
            print(tree1)
            print(tree2)
            update(1, 0, n - 1, c, l[b])
            print(tree1)
            print(tree2)
            l[b],l[c] = l[c],l[b]
        else:
            h = subSum(1, 0, n - 1, b, c)
            x = h[0]
            y = h[1]
            print(b,c,x,y)
            if b==x and c==y:
                print("YES")
            else:
                print("NO")
        print(l)
