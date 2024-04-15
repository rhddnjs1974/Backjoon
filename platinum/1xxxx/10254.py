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

T = int(input())
for i in range(T):
    n = int(input())
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
    ans = 0
    a = 0
    c = 1
    t = 0
    while(t<200000):
        t+=1
        distx = (convex_arr[a][0] - convex_arr[c][0]) ** 2
        disty = (convex_arr[a][1] - convex_arr[c][1]) ** 2
        if ans<(distx+disty)**0.5:
            ans2 = (a,c)
            ans = (distx+disty)**0.5

        b = (a+1)%l
        d = (c+1)%l
        p1 = convex_arr[a]
        p2 = convex_arr[b]
        p3_x = convex_arr[d][0]+convex_arr[b][0]-convex_arr[c][0]
        p3_y = convex_arr[d][1]+convex_arr[b][1]-convex_arr[c][1]
        p3 = (p3_x,p3_y)

        x = ccw(*p1,*p2,*p3)
        if x<0:
            a=(a+1)%l
            if a==0:
                break
        else:
            c=(c+1)%l

    print(*convex_arr[ans2[0]],*convex_arr[ans2[1]])