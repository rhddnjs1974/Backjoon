import math
n,r,g,b = map(int,input().split())
ans = 0
def facto(n):
    if n>1:
        return n*facto(n-1)
    return 1
def bt(n,r,g,b,now):
    global ans
    if n==0:
        ans += now
        return
    
    if n%3==0:
        if r>= n//3 and g>=n//3 and b>=n//3:
            bt(n-1,r-n//3,g-n//3,b-n//3,now*facto(n)//((facto(n//3))**3))
    if n%2==0:
        if r>= n//2 and g>=n//2:
            bt(n-1,r-n//2,g-n//2,b,now*facto(n)//((facto(n//2))**2))
        if g>= n//2 and b>=n//2:
            bt(n-1,r,g-n//2,b-n//2,now*facto(n)//((facto(n//2))**2))
        if r>= n//2 and b>=n//2:
            bt(n-1,r-n//2,g,b-n//2,now*facto(n)//((facto(n//2))**2))
    
    if r>=n:
        bt(n-1,r-n,g,b,now)
    if g>=n:
        bt(n-1,r,g-n,b,now)
    if b>=n:
        bt(n-1,r,g,b-n,now)
    
bt(n,r,g,b,1)
print(ans)