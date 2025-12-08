import math


def moduler_inverse(n,a): #모듈러 n에 대한 a의 곱셈 역원
    if math.gcd(n,a)!=1:
        return -1
    n2 = a
    a,b = a,n
    
    
    t1, t2 = 1, 0
    while b:
        q = a // b
        r = a - q*b
        a, b = b, r
        
        t = t1-q*t2
        t1, t2 = t2, t
    
    if t1<0:
        t1 = n+t1

    t2 = (1-t1*n2)//n
    
    return t2,t1

for _ in range(int(input())):   
    n, s, q = map(int,input().split())

    g = math.gcd(n,abs(s))
    q //= g

    a, b= moduler_inverse(n//g,s//g)

    a *= q
    b *= q

    x = -s//g
    y = n//g
    
    t = a//x
    
    
    a -= t*x
    b -= t*y

    if b<=0:
        t = -b//y
        a += t*x
        b += t*y
    if b<=0:
        a += x
        b += y
    
    print(a,b)