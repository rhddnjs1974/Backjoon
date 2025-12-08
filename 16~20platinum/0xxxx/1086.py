import sys
input = sys.stdin.readline
import math
def f(k,bit,l):
    if dp[k][bit]!=-1:
        return

    dp[k][bit] = 0
    if bit==t:
        if k==0:
            dp[k][bit] = 1
        else:
            dp[k][bit] = 0


    for i in range(N):
        if not bit&(1<<i):
            nk = (k+remain[i]*remain_l[l])%K

            f(nk,bit|(1<<i),l+L[i])
            dp[k][bit] += dp[nk][bit|(1<<i)]

N = int(input())

arr = []
for i in range(N):
    arr.append(input().rstrip())

K = int(input())

remain_l = []
for i in range(751):
    remain_l.append((10**i)%K)
remain = []
L = []
for i in arr:
    L.append(len(i))
    i = int(i)
    remain.append(i%K)


w = [[0]*N for i in range(N)]
for i in range(N):
    for j in range(N):
        if i==j:
            continue
        cost = (remain[i]*remain_l[L[j]]) + remain[j]
        w[i][j] = cost%K

t = (1<<N) -1

dp = [[-1] * (1<<N) for i in range(K)]
ans = f(0,0,0)

top = dp[0][0]
bottom = 1
for i in range(1,N+1):
    bottom *= i

gcd = math.gcd(top,bottom)
print("%d/%d"%(top//gcd,bottom//gcd))