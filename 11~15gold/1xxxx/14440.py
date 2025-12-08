import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
########################################
c = 100
def power(a,b):
    global n
    if b==1:
        for i in range(n):
            for j in range(n):
                a[i][j] %= c
        return a

    tmp = power(a,b//2)
    if b%2==0:
        return mat_mul(tmp,tmp)
    else:
        return mat_mul(mat_mul(tmp,tmp),a)

def mat_mul(A,B):
    global n
    C = [[0]*n for i in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
            C[i][j] %= c
    return C

n=2

x,y,a0,a1,m = map(int,input().split())

a = []
a.append([x,y])
a.append([1,0])

if m==0:
    print("%02d"%(a0))
else:
    array = power(a,m)
    print("%02d" %( (array[1][0]*a1+array[1][1]*a0)%100))