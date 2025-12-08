import math

def CRT(a1,n1,a2,n2):
    #x = n1*a + a1
    #n1*a + n2*b = a2-a1
    g = math.gcd(n1,n2)
    if (a2-a1)%g!=0:
        print(-1)
        exit()
    
    n1 //=g
    n2 //=g
    
    right = (a2-a1)//g
    
    a = moduler_inverse(n2,n1)
    #b = (1-n1*a)//n2
    
    a *= right
    #b *= right

    # x = n1*n2*t + a*n1 + a1
    return a*n1*g+a1,n1*n2*g #나머지, 모듈러

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

P1,P2,P3,X1,X2,X3 = map(int,input().split())
X4,P4 = CRT(X1,P1,X2,P2)
X, P = CRT(X3,P3,X4,P4)
t = X//P
X -= t*P
if X<=0:
    X+=P
if 0<X<1000000000:
    print(X)
else:
    print(-1)