import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
########################################
def power(a,b):
    global n
    if b==1:
        for i in range(n):
            for j in range(n):
                a[i][j] %=1000
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
            C[i][j] %= 1000
    return C

n, b = map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))

array = power(a,b)
for i in array:
    print(*i)