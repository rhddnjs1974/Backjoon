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

def cross(A,B,C,D):
    p = ccw(*A, *B, *C) * ccw(*A, *B, *D)
    q = ccw(*C, *D, *A) * ccw(*C, *D, *B)

    if p <= 0 and q <= 0:
        if p == 0 and q == 0:
            if min(A[0], B[0]) <= max(C[0], D[0]) and min(C[0], D[0]) <= max(A[0], B[0]) and min(A[1], B[1]) <= max(
                    C[1], D[1]) and min(C[1], D[1]) <= max(A[1], B[1]):
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0


T = int(input())
for aaa in range(1,T+1):
    flag = 1

    n,m = map(int,input().split())
    arr = []
    for i in range(n):
        a,b = map(int,input().split())
        arr.append((a,b))
    arr.sort()

    arr2 = []
    for i in range(m):
        a,b = map(int,input().split())
        arr2.append((a,b))
    arr2.sort()

    if n>=3:
        x = convex_hull(arr)
        arr.reverse()
        y = convex_hull(arr)
        convex1 = x[:-1] + y[:-1]
    else:
        convex1 = []
        for i in arr:
            convex1.append(i)

    l1 = len(convex1)

    if m>=3:
        x = convex_hull(arr2)
        arr2.reverse()
        y = convex_hull(arr2)
        convex2 = x[:-1] + y[:-1]
    else:
        convex2 = []
        for i in arr2:
            convex2.append(i)

    l2 = len(convex2)

    for i in range(l1):
        A = convex1[i-1]
        B = convex1[i]
        for j in range(l2):
            C = convex2[j-1]
            D = convex2[j]
            if cross(A,B,C,D)==1:
                flag=0
                break
        if flag==0:
            break

    if flag==1 and l1>=3:
        dots = convex2[0]
        if inside(convex1,dots):
            flag=0
    if flag==1 and l2>=3:
        dots = convex1[0]
        if inside(convex2,dots):
            flag=0

    if flag==1:
        print("YES")
    else:
        print("NO")