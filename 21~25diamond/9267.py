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


n, s, q = map(int,input().split())
if n==s==q==0 or s==q or n==q:
    print("YES")
    exit()
if n==0:
    if s!=0 and q%s==0:
        print("YES")
    else:
        print("NO")
    exit()
if s==0:
    if q%n==0:
        print("YES")
    else:
        print("NO") 
    exit()
g = math.gcd(n,abs(s))
if q%g!=0:
    print("NO") 
    exit()
q //= g

a, b= moduler_inverse(n//g,s//g)

a *= q
b *= q


x = s//g
y = n//g

flag = 0

t = b//y
t += 1

a += t*x
b -= t*y

aa = 0

while(a>0 and aa<10000000):
    aa+=1
    if b>0 and math.gcd(a,b)==1:

        flag=1
        break
    a -= x
    b += y


if flag==1:
    print("YES")
else:
    print("NO")