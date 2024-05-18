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


n = int(input())
ans = 0
for i in range(2,n+1):
    ans += int(phi(i))
print(ans)