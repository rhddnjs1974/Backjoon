import sys
input = sys.stdin.readline
import math
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

T = 0
while(True):
    T+=1
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

    convex_arr = x[:-1]+y[:-1]

    l = len(convex_arr)

    ans = 1e11
    for i in range(l):
        k = (i+1)%l
        t = 0
        p0 = convex_arr[i]
        p1 = convex_arr[k]
        for j in range(l):
            p2 = convex_arr[j]

            if p1[0]==p0[0]:
                dist = abs(p2[0]-p0[0])
            else:
                a, b = (p1[1] - p0[1]) / (p1[0] - p0[0]), -1
                c = -a * p0[0] + p0[1]
                dist = abs(a * p2[0] + b * p2[1] + c) / (a ** 2 + b ** 2) ** 0.5

            t = max(t,dist)
        ans = min(ans,t)
    ans = math.ceil(ans*100)/100
    print("Case %d: %.2f"%(T,ans))
