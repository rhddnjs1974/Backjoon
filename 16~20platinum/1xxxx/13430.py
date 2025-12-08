import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
########################################
p = 1000000007
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

n,k = map(int,input().split())
n+=2
a = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(i+1):
        a[i][j] = 1

if k==1:
    print(1)
else:
    array = power(a, k - 1)
    print(sum(array[n-1])%p)