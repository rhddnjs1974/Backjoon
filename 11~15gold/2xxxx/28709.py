import sys

input = sys.stdin.readline
INF = 10**18

T = int(input())

for _ in range(T):
    S = input().strip()

    if '*' not in S and (len(S) % 2 == 1):
        print("NO")
        continue

    lo = hi = 0
    ok = True

    for c in S:
        if c == '(':
            lo += 1
            hi += 1
        elif c == ')':
            lo = max(0, lo-1)
            hi -= 1
        elif c == '?':
            lo = max(0, lo-1)
            hi += 1
        else:
            lo = 0
            hi = INF

        if hi < 0:
            ok = False
            break
    if ok and lo == 0:
        print("YES")
    else:
        print("NO")
