import math
a,b = map(int,input().split())
a,b = min(a,b),max(a,b)
if a==b:
    print(1)
    exit()
x = 1e30
k = max(a,b)-min(a,b)
d= set()
d.add(1)
i =0
while(i*i<=k):
    i+=1
    if k%i==0:
        d.add(i)
        d.add(k//i)

d = list(d)
d.sort()


for i in d:
    r = a%i
    r = i-r
    y = math.lcm(a+r,b+r)
    if y<x:
        x = y
        ans = r

print(ans)