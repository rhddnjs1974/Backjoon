import sys
input = sys.stdin.readline

N = int(input())
ans = 0
s = set()
for i in range(N):
    a = input().rstrip()
    if a!="ENTER" and a not in s:
        ans+=1
        s.add(a)
    if a=="ENTER":
        s = set()
print(ans)