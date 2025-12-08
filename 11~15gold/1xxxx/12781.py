import sys
input = sys.stdin.readline

def ccw(x1,y1,x2,y2,x3,y3):
    c = (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
    return c

x1,y1,x2,y2,x3,y3,x4,y4 = map(int,input().split())
A = [x1,y1]
B = [x2,y2]

C = [x3,y3]
D = [x4,y4]

p = ccw(*A,*B,*C)*ccw(*A,*B,*D)
q = ccw(*C,*D,*A)*ccw(*C,*D,*B)

if p<0 and q<0:
    print(1)
else:
    print(0)