import sys
input = sys.stdin.readline

def phi(n,k):
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
        k*=(1-1/i)

    return k

for i in range(int(input())):
    a,b,n = map(int,input().split())

    if n==1:
        print("Case #"+str(i+1)+":", (b-a+1))
    else: 
        print("Case #"+str(i+1)+":", (int(phi(n,b+1)) - int(phi(n,a))) )