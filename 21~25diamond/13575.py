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
sys.setrecursionlimit(10**5)
########################################
def powerfft(c,b):
    global N
    if b==1:
        return c
    global cc
    
    if b%2==0:
        A = powerfft(c,b//2)
        fft(A)
        B = [0]*N
        for i in range(N):
            B[i] = A[i]*A[i]
        ifft(B)
        return B
    else:
        A = powerfft(c,b//2)
        fft(A)
        B = [0]*N
        for i in range(N):
            B[i] = A[i]*A[i]*cc[i]
        ifft(B)
        
        return B
                
N=500000
N = math.log2(N)
N = 2**(int(N)+2)

n,k = map(int,input().split())
arr = list(map(int,input().split()))

x = [0]*N
a = [0]*N

for i in arr:
    x[i] =1

cc = x[:]
fft(cc)

a = powerfft(x,k)

for i in range(N):
    if a[i]!=0:
        print(i,end=" ")
