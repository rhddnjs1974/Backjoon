import math


def moduler_inverse(n,a): #모듈러 n에 대한 a의 곱셈 역원
    if math.gcd(n,a)!=1:
        return "IMPOSSIBLE"
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
        t2 = t2-n2
    
    if t1>1000000000:
        t1-n
    
    if t1<0:
        return "IMPOSSIBLE"
    return t1

for i in range(int(input())):
    n, a = map(int,input().split())
    if n==a==1:
        print(2)
    elif n==1:
        print(1)
    elif a==1:
        if n==1000000000:
            print("IMPOSSIBLE")
        else:
            print(n+1)
    else:
        print(moduler_inverse(n,a))