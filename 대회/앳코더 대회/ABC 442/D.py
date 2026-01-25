import sys
input = sys.stdin.readline

def bit_add(i, delta):
    while i <= n:
        bit[i] += delta
        i += i & -i

def bit_sum(i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

n, Q = map(int, input().split())
arr = list(map(int, input().split()))

bit = [0] * (n + 1)
i = 1
while i <= n:
    bit_add(i, arr[i - 1])
    i += 1

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        x = q[1]
        v1 = arr[x - 1]
        v2 = arr[x]

        arr[x - 1] = v2
        arr[x] = v1

        bit_add(x, v2 - v1)
        bit_add(x + 1, v1 - v2)

    else:
        l = q[1]
        r = q[2]
        print(bit_sum(r) - bit_sum(l - 1))
