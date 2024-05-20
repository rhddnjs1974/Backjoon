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


n = int(input())
print(int(phi(n)))