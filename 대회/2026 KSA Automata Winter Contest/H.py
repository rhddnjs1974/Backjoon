import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = []
for _ in range(K):
    c, a = map(int, input().split())
    arr.append((c, a))

def size(c):
    y = (c-1) // 2
    if c%2==1:
        return y+1
    return y+2

arr.sort(key=lambda x: (size(x[0])) / x[1])

L = 1
ans = 0

for c, a in arr:
    L += (c-1) // 2
    if c%2==1:
        ans += a*L*2
        L += 1
    else:
        ans += a*(L*2+1)
        L += 2

print(ans)