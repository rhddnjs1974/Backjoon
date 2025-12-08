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
            if ccw(*p1,*p2,*p3)>=0:
                break
            convex.pop()
        convex.append(p3)
    return convex

n = int(input())
arr = []
for i in range(n):
    a,b,c = input().split()
    if c=="Y":
        a=int(a)
        b=int(b)
        arr.append((a,b))

arr.sort()
x = convex_hull(arr)
arr.reverse()
y = convex_hull(arr)

print(len(x)+len(y)-2)

for i in x[:-1]:
    print(*i)
for i in y[:-1]:
    print(*i)