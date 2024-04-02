import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
########################################
c = 1000000
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
b = int(input())
a = []
a.append([1,1])
a.append([1,0])

array = power(a,b)
print(array[1][0])