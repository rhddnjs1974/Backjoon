import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))

L = A[0]
R = A[-1]

steps = N - 2

for t in range(steps, 0, -1):
    if t == 1:
        L -= 1
        R -= 1
    else:
        if L >= R:
            L -= 1
        else:
            R -= 1

print(max(L, R))
