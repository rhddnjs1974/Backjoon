import math

def count(x):
    t = 0
    while(t*t<=x):
        t+=1
    return t-1
a,b = map(int,input().split())

n = b-a
t = count(b)-count(a)

g = math.gcd(n,t)
if t==0:
    print(0)
else:
    print(str(t//g)+"/"+str(n//g))