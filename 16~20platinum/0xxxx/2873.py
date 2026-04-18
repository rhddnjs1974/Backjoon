import sys
input = sys.stdin.readline

r, c = map(int, input().split())
grid = []
for i in range(r):
    grid.append(list(map(int, input().split())))

if r % 2 == 1:
    for i in range(r):
        if i > 0:
            print('D', end="")
        if i % 2 == 0:
            print('R' * (c-1), end="")
        else:
            print('L' * (c-1), end="")
    print()
elif c % 2 == 1:
    for j in range(c):
        if j > 0:
            print('R', end="")
        if j % 2 == 0:
            print('D' * (r-1), end="")
        else:
            print('U' * (r-1), end="")
    print()
else:
    mi = 1001
    sr = 0
    sc = 1
    for i in range(r):
        for j in range((i+1) % 2, c, 2):
            if grid[i][j] < mi:
                mi = grid[i][j]
                sr = i
                sc = j
    kk = sc // 2
    bb = sr // 2
    skip_tr = (sr % 2 == 0)
    pairs = c // 2
    blocks = r // 2
    for k in range(pairs):
        if k > 0:
            print('R', end="")
        if k < kk:
            print('D' * (r-1), end="")
            print('R', end="")
            print('U' * (r-1), end="")
        elif k == kk:
            for b in range(blocks):
                if b > 0:
                    print('D', end="")
                if b < bb:
                    print('RDL', end="")
                elif b == bb:
                    if skip_tr:
                        print('DR', end="")
                    else:
                        print('RD', end="")
                else:
                    print('LDR', end="")
        else:
            print('U' * (r-1), end="")
            print('R', end="")
            print('D' * (r-1), end="")
    print()
