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
        return

def ccw(x1,y1,x2,y2,x3,y3):
    c = (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
    return c

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = int(input())

parent = [0] * (N + 1)

for i in range(1, N + 1):
    parent[i] = i

arr = []
for i in range(N):
    arr.append(list(map(float,input().split())))


for i in range(N):
    for j in range(i+1,N):
        A = [arr[i][0], arr[i][1]]
        B = [arr[i][2], arr[i][3]]

        C = [arr[j][0], arr[j][1]]
        D = [arr[j][2], arr[j][3]]

        if cross(A,B,C,D):
            union(i,j)

a = set()
for i in range(N):
    a.add(find(i))
print(len(a))

