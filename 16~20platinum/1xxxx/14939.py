import sys
input = sys.stdin.readline

def popcount(x):
    return x.bit_count()

def apply(r, press):
    left = (press << 1) & FULL
    right = press >> 1
    a[r] ^= press ^ left ^ right
    if r > 0:
        a[r-1] ^= press
    if r < 9:
        a[r+1] ^= press

rows = []
for i in range(10):
    s = input().strip()
    mask = 0
    for i in range(10):
        if s[i] == 'O':
            mask |= 1 << i
    rows.append(mask)

FULL = (1 << 10) - 1
ans = 10**9

for first in range(1 << 10):
    a = rows[:]
    cnt = popcount(first)

    apply(0, first)

    for r in range(1, 10):
        press = a[r-1]
        cnt += popcount(press)
        apply(r, press)

    if a[9] == 0:
        ans = min(ans, cnt)

if ans==10**9:
    print(-1)
else:
    print(ans)

