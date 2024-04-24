import sys
input = sys.stdin.readline

pi = 3.14156295
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

n,l = map(int,input().split())
arr = []
for i in range(n):
    a,b = map(int,input().split())
    arr.append((a,b))

arr.sort()

x = convex_hull(arr)
arr.reverse()
y = convex_hull(arr)

ans = x[:-1] + y[:-1]
L = len(ans)
dist = 0
for i in range(L):
    j = (i+1)%L
    dist += ((ans[i][0]-ans[j][0])**2 + (ans[i][1]-ans[j][1])**2)**0.5

print(round(dist+2*pi*l))