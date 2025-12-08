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
            if ccw(p1[0],p1[1],p2[0],p2[1],p3[0],p3[1])>=0:
                break
            convex.pop()
        convex.append(p3)
    return convex

T = int(input())
for aa in range(T):
    x = list(map(int,input().split()))
    n = x[0]

    arr = [[] for i in range(n)]
    for i in range(1,n*2+1):
        t = (i-1)//2
        arr[t].append(x[i])
        if i%2==0:
            arr[t].append(t)


    arr.sort()
    x = convex_hull(arr)
    arr.reverse()
    y = convex_hull(arr)

    ans = x[:-1]+y[:-1]

    ans2 = []
    for i in ans:
        ans2.append(i[2])
    if aa==T-1:
        print(*ans2,end="")
    else:
        print(*ans2)

