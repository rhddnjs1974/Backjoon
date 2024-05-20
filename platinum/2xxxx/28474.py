import sys
input = sys.stdin.readline

def phi(n):
    N = n
    for i in range(2,1+N):
        if i*i>N:
            break
        if N%i==0:
            n = n/ i *(i-1)
            while(N%i==0):
                N=N//i
    if N>1:
        n = n / N * (N-1)
    return int(n)

T = int(input())
for _ in range(T):
    n = int(input())
    ans = phi(n)
    if n%2==0:
        ans+= phi(n//2)

    if n ==1:
        print(0)
    elif n==2:
        print(1)
    else:
        print(ans)