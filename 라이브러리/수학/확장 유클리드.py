import math
n, a = map(int,input().split())

def moduler_inverse(n,a): #모듈러 n에 대한 a의 곱셈 역원
    if math.gcd(n,a)!=1:
        return -1
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
    
    return t1

print(n-a,moduler_inverse(n,a))