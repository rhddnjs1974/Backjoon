import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    a,b = input().split()
    a = int(a)
    t = 0
    for i in b:
        t+=int(i)
    print(t%(a-1))