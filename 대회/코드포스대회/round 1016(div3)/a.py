import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    if n%2==0:
        print("NO")
    else:
        print("YES")