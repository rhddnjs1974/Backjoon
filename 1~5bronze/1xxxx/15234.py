import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

seen = set()
ans = 0

for x in arr:
    y = k - x
    if y in seen:
        ans += 1
    seen.add(x)

print(ans)
