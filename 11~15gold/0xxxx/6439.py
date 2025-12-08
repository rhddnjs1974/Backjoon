import sys
input = sys.stdin.readline

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


def ccw(x1,y1,x2,y2,x3,y3):
    c = (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
    return c

T = int(input())
for i in range(T):
    x1, y1, x2, y2,xl,yt,xr,yb = map(int, input().split())
    A = [x1,y1]
    B = [x2,y2]
    flag=0
    if min(xl,xr)<=x1<=max(xl,xr) and min(yt,yb)<=y1<=max(yt,yb):
        flag=1


    C = [xl, yt]
    D = [xr, yt]
    ans1 = cross(A,B,C,D)

    C = [xl, yb]
    D = [xr, yb]
    ans2 = cross(A, B, C, D)

    C = [xl, yt]
    D = [xl, yb]
    ans3 = cross(A, B, C, D)

    C = [xr, yt]
    D = [xr, yb]
    ans4 = cross(A, B, C, D)

    if ans1 or ans2 or ans3 or ans4 or flag:
        print("T")
    else:
        print("F")


