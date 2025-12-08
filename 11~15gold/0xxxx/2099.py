import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
########################################
p = 1000
def power(a,b):
    global n,p
    if b==1:
        for i in range(n):
            for j in range(n):
                if a[i][j]>p:
                    a[i][j] = 1
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
            if C[i][j]>p:
                C[i][j] = 1
    return C

n,k,m = map(int,input().split())

a = [[0]*n for i in range(n)]
for i in range(n):
    u,v = map(int,input().split())
    a[i][u-1] = 1
    a[i][v-1] = 1

array = power(a,k)


for i in range(m):
    a,b = map(int,input().split())
    if array[a-1][b-1]==0:
        print("life")
    else:
        print("death")