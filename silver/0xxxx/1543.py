import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

L = len(a)
l = len(b)

last = -50
ans = 0
for i in range(L-l+1):
    if i<last+l:
        continue

    if a[i:i+l] == b:
        ans+=1
        last = i

print(ans)