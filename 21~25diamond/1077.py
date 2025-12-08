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

n,m = map(int,input().split())

arr = []
for i in range(n):
    a,b = map(int,input().split())
    arr.append((a,b))


arr2 = []
for i in range(m):
    a,b = map(int,input().split())
    arr2.append((a,b))

ans = []
for i in range(n):
    A = arr[i-1]
    B = arr[i]
    for j in range(m):
        C = arr2[j-1]
        D = arr2[j]

        x1,y1 = A
        x2,y2 = B
        x3,y3 = C
        x4,y4 = D
        if cross(A,B,C,D):
            try:
                x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / (
                            (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
                y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / (
                            (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
                ans.append((x, y))
            except:
                if A > B:
                    A, B = B, A
                if C > D:
                    C, D = D, C
                if B == C:
                    ans.append((B[0], B[1]))
                elif A == D:
                    ans.append((A[0], A[1]))

for i in arr:
    if inside(arr2,i):
        ans.append(i)

for i in arr2:
    if inside(arr,i):
        ans.append(i)


ans.sort()
x1 = convex_hull(ans)
ans.reverse()
x2 = convex_hull(ans)
ans = x1[:-1]+x2[:-1]

print(find_area(ans))
