import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
########################################
def power(a,b):
    global n
    if b==1:
        for i in range(n):
            for j in range(n):
                a[i][j] %=1000000007
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
            C[i][j] %= 1000000007
    return C

m = int(input())
n=2
if m%2==1:
    print(0)
else:
    a = []
    t = m//2
    a.append([4,-1])
    a.append([1,0])


    array = power(a,t)

    ans = array[1][0]*3+array[1][1]
    print(ans%1000000007)