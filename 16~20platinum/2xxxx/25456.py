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
            

n = 500000
n = math.log2(n)
n = 2**(int(n)+2)

a = [0]*n

ii = input().rstrip()
jj = input().rstrip()

x = []
for i in ii:
    x.append(int(i))
x = x+x
y = []
for i in jj:
    y.append(int(i))
y = y[::-1]

x += ( n-len(x) ) * [0]
y += ( n-len(y) ) * [0]

fft(x)
fft(y)

for i in range(n):
    a[i] = x[i]*y[i]

ifft(a)
print(max(a))
