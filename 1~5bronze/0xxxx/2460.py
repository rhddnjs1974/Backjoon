import sys
input = sys.stdin.readline

c = 0
ans = 0

for _ in range(10):
    a, b = map(int, input().split())
    c -= a
    c += b
    if c > ans:
        ans = c

print(ans)