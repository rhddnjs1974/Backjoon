import sys
input = sys.stdin.readline

def ccw(x1,y1,x2,y2,x3,y3):
    c = (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
    return c

x1,y1,x2,y2 = map(int,input().split())
A = [x1,y1]
B = [x2,y2]
x3,y3,x4,y4 = map(int,input().split())
C = [x3,y3]
D = [x4,y4]

p = ccw(*A,*B,*C)*ccw(*A,*B,*D)
q = ccw(*C,*D,*A)*ccw(*C,*D,*B)

if p<=0 and q<=0:
    print(1)
else:
    print(0)


################스치듯 만나는것도 교차####################

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

x1,y1,x2,y2 = map(int,input().split())
A = [x1,y1]
B = [x2,y2]
x3,y3,x4,y4 = map(int,input().split())
C = [x3,y3]
D = [x4,y4]

print(cross(A,B,C,D))