import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    B = list(map(int,input().split()))
    b = set()
    for i in B:
        b.add(i)
    print(len(b))