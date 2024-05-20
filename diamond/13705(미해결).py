import sys
input = sys.stdin.readline
import math

def cal(x):
    global a,b
    y = x*a+b*math.sin(x)
    return y
a,b,c = map(int,input().split())

l = (c-b)/a
r = (c+b)/a
while(l<=r-0.0000000001):
    mid = (l+r)/2
    ret = cal(mid)
    if ret>c:
        r = mid
    else:
        l = mid

print("%.6f"%(mid))