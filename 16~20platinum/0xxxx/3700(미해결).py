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

def inside(shape,dot):
    a,b = dot
    C = [a,b]
    D = [1000000001,b+1] #최대x +1,해당y+1
    t=0
    for j in range(len(shape)):
        A=shape[j]
        B=shape[(j+1)%len(shape)]
        t+= cross(A,B,C,D)
        if cross(A,B,C,C)==1:
            t=1
            break
        if A[0]==C[0] and A[1]==C[1]:
            t=1
            break
    return t%2
    
for _ in range(int(input())):
    N = int(input())
    ans = []
    for i in range(N):
        h,l,*x = list(map(int,input().split()))
        arr=[]
        for j in range(l):
            arr.append((x[j*2],x[j*2+1]))
        sy= inside(arr,(0,0))
        sg= inside(arr,(100000,0))
        ans.append((h,sy,sg))
    print(ans)