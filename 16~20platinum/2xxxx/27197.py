import sys
from bisect import bisect_right
input = sys.stdin.readline

n,B,C = map(int,input().split())
x = [0]*n
p = [0]*n
for i in range(n):
    a,b = map(int,input().split())
    x[i] = a
    p[i] = b

def ok(d):
    k = bisect_right(x,d)
    xx = x[:k]
    pp = p[:k]
    xx.append(d)
    pp.append(0)
    m = len(xx)

    for i in range(m-1):
        if xx[i+1]-xx[i] > C:
            return False

    next = [m-1]*m
    st = []
    for i in range(m-1,-1,-1):
        while st and pp[st[-1]] >= pp[i]:
            st.pop()
        if st:
            next[i] = st[-1]
        st.append(i)

    fuel = 0
    cost = 0
    for i in range(m-1):
        need = C
        if xx[next[i]]-xx[i] <= C:
            need = xx[next[i]]-xx[i]
            
        if fuel < need:
            buy = need-fuel
            cost += buy * pp[i]
            if cost > B:
                return False
            fuel = need
        fuel -= (xx[i+1]-xx[i])
    return True

l = 0
r = x[-1]+C
while l < r:
    mid = (l+r+1)//2
    if ok(mid):
        l = mid
    else:
        r = mid-1
print(l)