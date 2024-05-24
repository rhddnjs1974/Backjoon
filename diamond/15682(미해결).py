import sys
input = sys.stdin.readline
from decimal import *
getcontext().prec = 100

def fun(l,r):
    global ans
    if cal(l) < cal(r):
        graph = "inc"
    else:
        graph = "dec"
    mid = -1e9
    while (abs(l - r) > Decimal('0.00000000000000000001')):
        mid = (l + r) / Decimal('2')
        ret = cal(mid)
        if graph == "inc":
            if ret > 0:
                r = mid
            else:
                l = mid
        else:
            if ret > 0:
                l = mid
            else:
                r = mid

    if mid==-1e9:
        if cal(l)==0:
            ans.add(l)
    else:

        ans.add(mid)

def cal(x):
    global a,b,c,d
    y = a*x**3+b*x**2+c*x+d
    return y

T = int(input())
for case in range(T):
    a,b,c,d = map(float,input().split())
    a = Decimal(a)
    b = Decimal(b)
    c = Decimal(c)
    d = Decimal(d)

    D = b**2-3*a*c
    ans = set()
    if D<0:
        l = Decimal('-1000000')
        r = Decimal('1000000')
        fun(l,r)
    else:
        dx1 = (-b+D**Decimal('0.5'))/(Decimal('3')*a)
        dx2 = (-b-D**Decimal('0.5'))/(Decimal('3')*a)
        if a<0:
            dx1,dx2 = dx2,dx1


        l = Decimal('-1000000')
        r = dx2
        if cal(r)*cal(l)<=0:
            fun(l, r)

        l = dx2
        r = dx1
        if cal(r)*cal(l)<=0:
            fun(l, r)

        l = dx1
        r = Decimal('1000000')
        if cal(r)*cal(l)<=0:
            fun(l, r)

    ans = list(ans)
    ans2 = [ans[0]]
    for i in ans[1:]:
        if abs(ans2[-1]-i)<0.00000000001:
            continue
        ans2.append(i)
    ans2.sort()
    for i in ans2:
        if abs(i)<0.00000000001:
            i = 0
        print(round(i,20),end=" ")
    if case!=T-1:
        print()