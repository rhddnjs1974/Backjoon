import math
mod = 1000000007
f = [0,1,1]
for i in range(100000):
    f.append((f[-1]+f[-2])%mod)
ans=0
n= int(input())
for i in range(2,n+2):
    g = math.gcd(n+1,i)
    ans+=f[g]
    ans %= mod

print(ans)