import sys
input = sys.stdin.readline

n, k = map(int, input().split())
h = list(map(int, input().split()))

l = [0] * (n-1)
for i in range(n-1):
    x = abs(h[i]-h[i+1])
    l[i] = (x * n)+i

l.sort(reverse=True)

arr = [0] * n
c = 0
i = 0
m = n-1
ans = 0

while i < m:
    x = l[i]
    d = x // n
    while i < m and (l[i] // n) == d:
        p = l[i] % n
        if arr[p] == 0:
            arr[p] = 1
            c += 1
        
        if arr[p+1] == 0:
            arr[p+1] = 1
            c += 1
            
        i += 1
        
    if c > k:
        ans = d
        break

print(ans)