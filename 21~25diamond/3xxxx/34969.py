import sys
input = sys.stdin.readline

mod = 998244353 #주어진 소수
def p(n,r):
    if n < r or r < 0:
        return 0
    return fac[n] * invfac[n-r] % mod

n,m = map(int,input().split())

fac = [1] * (m+1)
for i in range(1,m+1):
    fac[i] = fac[i-1] * i % mod

invfac = [1] * (m+1)
invfac[m] = pow(fac[m], mod-2, mod)
for i in range(m,0,-1):
    invfac[i-1] = invfac[i] * i % mod

ans = 0
for i in range(1,n+1):
    ans += p(m,i) * p(m-1,n-i) % mod
    if i==1:
        continue

    ans -= p(m-1,i-1) * p(m-1,n-i+1) % mod
    ans %= mod

print(ans)