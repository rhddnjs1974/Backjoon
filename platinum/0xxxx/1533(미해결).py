import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
########################################
cc = 1000003
def power(a,b):
    global n
    if b==1:
        for i in range(n):
            for j in range(n):
                a[i][j] %= cc
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
            C[i][j] %= cc
    return C



n,s,e,T = map(int,input().split())

A = []
for i in range(n):
    t = input().rstrip()
    A.append([])
    for j in t:
        A[i].append(int(j))

print(A)
print(T)
ANS = power(A,1)
print(ANS)