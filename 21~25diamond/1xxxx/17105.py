import sys
input = sys.stdin.readline
import math

p = 998244353
def fft(a):
    n = len(a)
    j = 0
    for i in range(1,n):
        reverse = n // 2
        while j >= reverse:
            j -= reverse
            reverse //= 2
        j += reverse
        if i < j:
            a[i], a[j] = a[j], a[i]
    
    step = 2
    while step <= n: 
        half = step // 2
        u = pow(3, p//step, p)
        
        for i in range(0, n, step):
            w = 1
            for j in range(i, i + half):
                v = a[j + half] * w
                a[j + half] = (a[j] - v)% p
                a[j] = (a[j]+v) % p
                w = (u*w) % p
        step *= 2


def ifft(a):
    n = len(a)
    j = 0
    for i in range(1,n):
        reverse = n // 2
        while j >= reverse:
            j -= reverse
            reverse //= 2
        j += reverse
        if i < j:
            a[i], a[j] = a[j], a[i]
    
    step = 2
    while step <= n: 
        half = step // 2
        u = pow(3, p//step, p)
        u = pow(u, p-2,p)
        for i in range(0, n, step):
            w = 1
            for j in range(i, i + half):
                v = a[j + half] * w
                a[j + half] = (a[j] - v)% p
                a[j] = (a[j]+v) % p
                w = (u*w) % p
        step *= 2

    num = p - (p-1) // n
    for i in range(n):
        a[i] = (a[i] * num) %p
            


def primeList(n):
    n+=1
    arr = [0,0] + [1]*n

    for i in range(2,int(n**0.5)+1):
        if arr[i]==1:
            for j in range(i*2,n+1,i):
                arr[j] = 0

    return arr


x = primeList(1000002)

n=1000000
n = math.log2(n)
n = 2**(int(n)+2)

F = [0]*n
G = [0]*n
Z = [0]*n

Y = [0]*n

for i in range(2,1000002):
    if x[i]==1:
        F[i] = 1
    if i*2<1000003 and x[i]==1:
        G[i*2] = 1
    if i*3<1000003 and x[i]==1:
        Z[i*3] = 1
        
fft(F)
fft(G)

for i in range(n):
    G[i] *= F[i]
    F[i] *= F[i]*F[i]
    

ifft(F) #6a+3b+c
ifft(G) #b+c
# Z : c

for _ in range(int(input())):
    N = int(input())
    A =F[N]
    B =G[N]
    C =Z[N]

    c =C
    b = B-c
    a = (A-3*b-c)//6
    print(a+b+c)
    



