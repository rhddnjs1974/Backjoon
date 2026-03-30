import sys
input = sys.stdin.readline

n, m = map(int, input().split())

fact = [1]*(n+1)
for i in range(1, n+1):
    fact[i] = (fact[i-1] * i) % m

invfact = [1]*(n+1)
invfact[n] = pow(fact[n], m-2, m)
for i in range(n, 0, -1):
    invfact[i-1] = (invfact[i] * i) % m

inv2 = pow(2, m-2, m)
total = pow(n, n-2, m)
ans = 0

for k in range(1, (n//2)+1):
    a = 1
    if k > 1:
        a = pow(k, k-2, m)

    b = 1
    if n-k > 1:
        b = pow(n-k, n-k-2, m)

    ways = fact[n]
    ways = (ways * invfact[k]) % m
    ways = (ways * invfact[n-k]) % m
    ways = (ways * k) % m
    ways = (ways * (n-k)) % m
    ways = (ways * a) % m
    ways = (ways * b) % m

    if k*2 == n:
        ways = (ways * inv2) % m

    ans += k * ways
    ans %= m

ans = (ans * pow(total, m-2, m)) % m
print(ans)