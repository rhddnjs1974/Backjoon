import sys
input = sys.stdin.readline

def inside(shape,dot):
    area1 = find_area(shape)
    area2 = 0

    for i in range(len(shape)):
        a = ccw(*shape[i-1],*shape[i],*dot)
        area2 += abs(a/2)

    if area1==area2:
        return 1
    else:
        return 0

def find_area(array):
    area = 0
    for i in range(1, len(array)-1):
        area += ccw(*array[0], *array[i], *array[i + 1])
    area = abs(area)
    return area*0.5
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

n,px,py = map(int,input().split())
arrs = []
for i in range(n):
    a,b = map(int,input().split())
    arrs.append((a,b))

use = set()
a = 0
while(True):

    arr = []
    for i in arrs:
        if i not in use:
            arr.append(i)

    arr.sort()

    x = convex_hull(arr)
    arr.reverse()
    y = convex_hull(arr)

    convex = x[:-1]+y[:-1]
    for i in convex:
        use.add(i)
    t = inside(convex,(px,py))

    if not convex or not t:
        break
    a += 1
print(a)