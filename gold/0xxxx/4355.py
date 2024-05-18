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

while(True):
    n = int(input())
    if n==0:
        break
    if n==1:
        print(0)
    else:
        print(int(phi(n)))