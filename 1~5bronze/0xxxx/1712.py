import math
a,b,c = map(int,input().split())

if b>=c:
    print(-1)
else:
    x = (a) // (c-b)
    if x==int(x):
        print(x+1)
    else:
        print(int(x)+1)