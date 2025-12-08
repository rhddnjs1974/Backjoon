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

n, m = map(int,input().split())
arr = [[0]*n for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1

d = int(input())
array = power(arr,d)
print(array[0][0])