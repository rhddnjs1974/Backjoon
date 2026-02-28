import sys
input = sys.stdin.readline

MOD = 1000000007

def ncr(n, r):
    if r<0 or r>n:
        return 0
    x = facto[n] * invfacto[r] % MOD
    return  x * invfacto[n-r] % MOD

arr = []
maxn = 0

for testcase in range(int(input())):
    n, x = map(int, input().split())
    oper = input().split()
    arr.append((n, x, oper))
    
    maxn = max(maxn,n)

facto = [1] * (maxn+1)
for i in range(1, maxn+1):
    facto[i] = facto[i-1] * i % MOD

invfacto = [1] * (maxn+1)
invfacto[maxn] = pow(facto[maxn], MOD - 2, MOD)

for i in range(maxn, 0, -1):
    invfacto[i-1] = (invfacto[i]*i) % MOD

for n, x, oper in arr:
    marr = []
    
    onlypm = 0
    for o in oper:
        what = o[0]
        y = int(o[1:])
        
        if what == '+':
            onlypm = (onlypm+y) % MOD
        elif what == '-':
            onlypm = (onlypm-y) % MOD
        elif what == 'x':
            marr.append(y % MOD)
        else:
            marr.append(pow(y % MOD, MOD - 2, MOD))

    m = len(marr)
    a = n-1 - m

    A = 1
    for t in marr:
        A = A * t % MOD

    arr2 = [0] * (m + 1)
    arr2[0] = 1
    for f in marr:
        for k in range(m, 0, -1):
            arr2[k] = (arr2[k] + arr2[k-1] * f) % MOD

    arr3 = [0] * n
    for k in range(m + 1):
        if arr2[k] == 0:
            continue
        
        for t in range(k, k+a+1):
            arr3[t] = (arr3[t] + arr2[k] * ncr(a, t-k)) % MOD

    invn = pow(n, MOD-2, MOD)
    now = 0
    for t in range(n):
        now = (now + arr3[t] * pow(ncr(n-1, t), MOD - 2, MOD)) % MOD
    y = now * invn % MOD

    ans = (A * (x % MOD) + y * onlypm) % MOD
    
    
    print(ans)
