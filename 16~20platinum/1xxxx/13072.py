import sys
input = sys.stdin.readline

def ccw(x1,y1,x2,y2,x3,y3):
    c = (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
    return c

def convex_hull(position):
    convex = []
    for p3 in position:
        while len(convex)>=2:
            p1,p2 = convex[-2],convex[-1]
            if ccw(*p1,*p2,*p3)>0:
                break
            convex.pop()
        convex.append(p3)
    return convex


while(True):
    n = int(input())
    if n==0:
        break
    arr = []
    for i in range(n):
        a,b = map(int,input().split())
        arr.append((a,b))

    arr.sort()

    x = convex_hull(arr)
    arr.reverse()
    y = convex_hull(arr)

    t = x + y[1:]
    a = 0
    b = 0
    for i in range(len(t)-1):
        x,y = t[i]
        x2,y2 = t[i+1]
        
        xx = abs(x2-x)
        yy = abs(y2-y)
        x, y = min(xx,yy),max(xx,yy)
        b+=x
        a+=(y-x)

    print(a,b)