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
            
n=100000
n = math.log2(n)
n = 2**(int(n)+2)

x = [0]*n
a = [0]*n
m = int(input())

for i in range(1,m):
    x[(i*i)%m] +=1

y = x[:]
fft(x)

for i in range(n):
    a[i] = x[i]*x[i]

ifft(a)
ans = 0
for i in range(m):
    if y[i]!=0:
        ans+=a[i]

print(y[:m])
print(a[:m*3])
print(ans)