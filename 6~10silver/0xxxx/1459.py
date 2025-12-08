import sys
input = sys.stdin.readline

x,y,w,s = map(int,input().split())

if s<w:
    mi = min(x, y)
    mii = max(x, y) - mi
    if mii%2==0:
        print(mi * s + mii * s)
    else:
        print(mi * s + mii * s - s + w)

elif s>=w*2:
    print(w*(x+y))
else:
    mi = min(x,y)
    mii = max(x,y)-mi
    print(mi*s+mii*w)