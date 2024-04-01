import sys
input = sys.stdin.readline

def ccw(x1,y1,x2,y2,x3,y3):
    c = (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
    return c

x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())

t = ccw(x1,y1,x2,y2,x3,y3)
if t>0:
    print(1)
elif t<0:
    print(-1)
else:
    print(0)