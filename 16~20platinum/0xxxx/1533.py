import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
########################################
p = 1000003
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

n, S, E, T = map(int,input().split())
arr = []
for i in range(n):
    s = input().rstrip()
    arr.append([])
    for j in s:
        j = int(j)
        arr[i].append(j)


a = [[0]*n*5 for i in range(n*5)]
for i in range(n*5):
    if i%5==0:
        continue
    a[i][i-1] = 1

for i in range(n):
    for j in range(n):
        if arr[i][j]==0:
            continue
        t = arr[i][j]
        a[i*5][j*5+t-1] = 1

n*=5
array = power(a,T)

S-=1
E-=1
S*=5
E*=5
print(array[S][E])