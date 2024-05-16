import sys
input = sys.stdin.readline

n,m = map(int,input().split())

pack = 1e9
one = 1e9
for i in range(m):
    a,b = map(int,input().split())
    pack = min(pack,a)
    one = min(one,b)

if pack>=one*6:
    print(n*one)
else:
    t = n//6
    p = n%6
    if pack<one*p:
        print(pack*t+pack)
    else:
        print(pack*t+p*one)