import sys
input = sys.stdin.readline


def ok(t):
    lo = 0
    hh = t
    for i in range(n):
        d = a[i] - b[i]
        rr = x[i] - (t * b[i])
        if d == 0:
            if rr < 0:
                return False
        else:
            if d > 0:
                uh = rr // d
                if uh < hh:
                    hh = uh
            else:
                ul = -((-rr) // d)
                if ul > lo:
                    lo = ul
        if lo > hh:
            return False
        
    if lo < 0:
        lo = 0
    if hh > t:
        hh = t
        
    return lo <= hh

n = int(input())
x = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

hi = -1
for i in range(n):
    m = min(a[i],b[i])
    v = x[i] // m

    hi = max(hi,v)


l = 0
r = hi
ans = 0
while l <= r:
    m = (l + r) // 2
    if ok(m):
        ans = m
        l = m+1
    else:
        r = m-1

print(ans)