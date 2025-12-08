import math

n, m = map(int,input().split())
if n==1 or m==1:
    print(max(n,m))
    exit()

g = math.gcd(n-1,m-1)
print( (((n-1)//g)+1)*(((m-1)//g)+1) // 2+((n-1)//g)*((m-1)//g)*(g-1))