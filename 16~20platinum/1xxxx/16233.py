import sys

input = sys.stdin.readline
p = 0

def mod(n):
    r = 999999999
    x = 0
    while r:
        q = n // r
        if q > 9:
            return -1
        x = (x + q) * 10
        n %= r
        r //= 10
    return x

T = int(input())
ansarr = []

for _ in range(T):
    N = int(input())
    if N % 9:
        ansarr.append(-1)
    else:
        ansarr.append(mod(N))

print(*ansarr)