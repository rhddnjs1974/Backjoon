import math

n, m = map(int,input().split())

n =abs(n)
m =abs(m)
if n==m==0:
    print(0)
elif math.gcd(n,m)==1:
    print(1)
else:
    print(2)