import math

def CRT(a1,n1,a2,n2):
    #x = n1*a + a1
    #n1*a + n2*b = a2-a1
    g = math.gcd(n1,n2)
    if (a2-a1)%g!=0:
        return -1
    
    n1 //=g
    n2 //=g
    
    right = (a2-a1)//g
    
    a = moduler_inverse(n2,n1)
    #b = (1-n1*a)//n2
    
    a *= right
    #b *= right

    # x = n1*n2*t + a*n1 + a1
    return a*n1*g+a1,n1*n2*g

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

a,b,c,d,e,f,g = map(int,input().split())

arr = []
h=0
while(a>0 and b>0):
    v = h*(a)*b
    arr.append(v)
    h+=1
    a-=2
    b-=2

arr.sort()

n1 = arr[-1]
n2 = arr[-2]
n3 = arr[-3]

x,n4 = CRT(c,n1,d,n2)
x,n = CRT(e,n3,x,n4)

x = x%n
while(True):
    if f<=x<=g:
        break
    x+=n
print(x)