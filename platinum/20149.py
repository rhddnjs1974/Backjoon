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
flag = 0
if p<=0 and q<=0:
    if p==0 and q==0:
        if min(A[0],B[0])<=max(C[0],D[0]) and min(C[0],D[0])<=max(A[0],B[0]) and min(A[1],B[1])<=max(C[1],D[1]) and min(C[1],D[1])<=max(A[1],B[1]):
            print(1)
            flag = 1
        else:
            print(0)
    else:
        print(1)
        flag = 1
else:
    print(0)

if flag==1:
    try:
        x = ((x1*y2-y1*x2) * (x3-x4) - (x1-x2) * (x3*y4-y3*x4)) / ((x1-x2)*(y3-y4) - (y1-y2) * (x3-x4))
        y = ((x1*y2-y1*x2) * (y3-y4) - (y1-y2) * (x3*y4-y3*x4)) / ((x1-x2)*(y3-y4) - (y1-y2) * (x3-x4))
        print(x,y)
    except:
        if A>B:
            A,B=B,A
        if C>D:
            C,D=D,C
        if B==C:
            print(B[0],B[1])
        elif A==D:
            print(A[0],A[1])