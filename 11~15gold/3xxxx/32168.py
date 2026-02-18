import sys
input = sys.stdin.readline

def interval_sum(a, b):
    return (a + b) * (b - a + 1) // 2

def subtree_sum(v, n):
    s = 0
    l = v
    r = v
    while l <= n:
        if r > n:
            s += interval_sum(l, n)
        else:
            s += interval_sum(l, r)
        l <<= 1
        r = (r << 1) | 1
    return s

def is_ancestor(a, b):
    while b > a:
        b //= 2
    return b == a

def child_on_path(a, b):
    prev = b
    while b != a:
        prev = b
        b //= 2
    return prev

n, q = map(int, input().split())

total = interval_sum(1, n)
root = 1

for _ in range(q):
    t, v = map(int, input().split())

    if t == 1:
        root = v
    else:
        if v == root:
            print(total)
        else:
            if not is_ancestor(v, root):
                print(subtree_sum(v, n))
            else:
                c = child_on_path(v, root)
                print(total - subtree_sum(c, n))
