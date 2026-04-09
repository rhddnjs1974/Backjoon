import math
from decimal import Decimal, getcontext
n, k = map(int,input().split())
getcontext().prec = 30

def small(n,k):
    ans = Decimal(0)
    nd = Decimal(n)
    for i in range(n-k+1,n+1):
        ans+= nd/Decimal(i)
    return ans

def smallH(n):
    ans = 0
    for i in range(1,n+1):
        ans+= 1/i
    return ans

def H(n):
    if n<=1000000:
        return smallH(n)
    ln = math.log(n)
    mas = 0.57721566490153286060651209008240243104215933593992

    return (math.log1p(n-1)+mas+(0.5/n)-(1/(12*n*n)) +(1/(120*n*n*n*n)))

def taylor(n,k):
    ans = 0
    pow = n*k/((n-k))
    for i in range(1,100001):
        if i%2==0:
            j=-1
        else:
            j=1
        ans += pow/(j*i)
        pow = pow*k/(n-k)
        if pow==0:
            break
    return ans
    
    
if k<2000000:
    print(small(n,k))
elif k<10000000000000 and k<n/10:
    print(taylor(n,k)+ 0.5 - 0.5*n/(n-k) + 1/(12*n) - n/(12*(n-k)*(n-k)) )
else:
    print(n*(H(n)-H(n-k)))