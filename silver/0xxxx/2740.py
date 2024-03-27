import sys
input = sys.stdin.readline

N,M = map(int,input().split())
A = []
for i in range(N):
    A.append(list(map(int,input().split())))

M,K = map(int,input().split())
B = []
for i in range(M):
    B.append(list(map(int,input().split())))

ANS = [[0]*K for i in range(N)]
for i in range(N):
    for j in range(K):
        for l in range(M):
            ANS[i][j] += A[i][l] * B[l][j]

for i in ANS:
    print(*i)