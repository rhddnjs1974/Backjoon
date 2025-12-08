import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)
########################################
p = 1000000009
def power(a,b):
    global n,p
    if b==1:
        for i in range(n):
            for j in range(n):
                a[i][j] %= p
        return a

    tmp = power(a,b//2)
    if b%2==0:
        return mat_mul(tmp,tmp)
    else:
        return mat_mul(mat_mul(tmp,tmp),a)

def mat_mul(A,B):
    global n,p
    C = [[0]*n for i in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
            C[i][j] %= p
    return C

T = int(input())
for _ in range(T):
    aa,b,c,d = map(int,input().split())
    c+=2
    a = [[0]*c for i in range(c)]
    for i in range(c):
        for j in range(i+1):
            a[i][j] = 1

    a[0][1] = 1
    a[0][0] = 0

    n=c
    if d==1:
        print(aa)
    else:
        array = power(a, d - 1)
        u = sum(array[n-1][1:])*aa
        v = array[n-1][0]*(b-aa)
        print((u+v)%p)