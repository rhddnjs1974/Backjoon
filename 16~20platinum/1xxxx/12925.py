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

n=2

T = int(input())
A = []
A.append([3,5])
A.append([1,3])
for i in range(T):
    b = int(input())
    ans = power(A,b)
    r = ans[0][0]*2-1
    r %= 1000
    print("Case #%d: %03d"%(i+1,r))
