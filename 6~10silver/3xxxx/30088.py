import sys
input = sys.stdin.readline

n = int(input())
s = []
for _ in range(n):
    m,*arr = map(int, input().split())
    s.append(sum(arr))
s.sort()

now = 0
ans = 0
for x in s:
    now += x
    ans += now

print(ans)