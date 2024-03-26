import sys
input = sys.stdin.readline

N = int(input())
s = set()
s.add("ChongChong")
ans = 1
for i in range(N):
    a,b = input().split()

    if a in s:
        s.add(b)
    elif b in s:
        s.add(a)
print(len(s))
