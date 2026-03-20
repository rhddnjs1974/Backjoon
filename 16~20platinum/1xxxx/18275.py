import sys
input = sys.stdin.readline

n,m = map(int, input().split())

p = 1
while p < n:
    p *= 2

seg = [0] * (2 * p)

for i in range(n):
    seg[p+i] = 1
for i in range(p-1, 0, -1):
    seg[i] = seg[i*2] + seg[i*2+1]

for y in range(m, m+n):
    v = 1
    bit = p // 2
    x = 0
    
    while v < p:
        if (y & bit) != 0 and seg[v*2+1] > 0:
            v = v*2+1
            x += bit
        else:
            v = v*2
            
        bit //= 2

    print(x, y)

    v = p+x
    seg[v] = 0
    v //= 2
    while v >= 1:
        seg[v] = seg[v*2] + seg[v*2+1]
        v //= 2