import sys
input = sys.stdin.readline
from decimal import *
getcontext().prec = 50

def sin(x):
    x = x%(Decimal('3.1415926535897932384626433832795028841971')*Decimal('2'))
    ans = x
    t = 1
    p = 1
    q = x
    i = 1
    lastans = -9999

    while(abs(lastans-ans)>Decimal('0.000000000000000000000000000000000001') and i<1000):
        lastans = ans
        i+=2
        p *= i*(i-1)
        q *= x*x
        t *= -1
        ans += (t*q/p)

    return ans

def cal(x):
    global a,b
    y = x*a+b*sin(x)
    return y
a,b,c = map(int,input().split())

l = Decimal('0')
r = Decimal('150000')
while(l<=r-Decimal('0.000000000000000000000000001')):
    mid = (l+r)/Decimal('2')
    ret = cal(mid)
    if ret>c:
        r = mid
    else:
        l = mid


print(round(mid,6))