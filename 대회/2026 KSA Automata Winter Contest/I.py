import sys
import math
input = sys.stdin.readline

N, Q = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split())) + [0]

need = [0] * (N+2)

def calculate():
    need[N+1] = 0
    for i in range(N,0,-1):
        v = need[i+1] - A[i]
        if v < 0:
            v = 0
        need[i] = v

for _ in range(Q):
    t, *aa = map(int, input().split())
    calculate()

    if t == 1:
        x, y = aa
        A[x] += y
    else:
        k = aa[0]
        if k < need[1]:
            print(-1)
        else:
            cost = 0
            for i in range(1, N):
                v = need[i + 1] - B[i]
                if v > 0:
                    cost += v
            print(cost)