import sys
input = sys.stdin.readline

def phi(n):
    N = n
    p = set()
    for i in range(2,1+int(N**0.5)):
        if i>N:
            break
        if N%i==0:
            p.add(i)
            while(N%i==0):
                N=N//i
    if N!=1:
        p.add(N)
    p = list(p)

    for i in p:
        n*=(1-1/i)
    return n

t = int(input())
ans = 2
dp=[1,2]
for i in range(2,10001):
    ans += int(phi(i))
    dp.append(ans)

for _ in range(t):
    n = int(input())
    print(dp[n])