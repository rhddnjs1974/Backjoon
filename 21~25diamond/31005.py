import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

MOD = 1000000007

n,m = map(int,input().split())

size = 2*n+5
parent = [i for i in range(size)]

def find(x):
    if parent[x] == x:
        return x

    path = []
    y = x
    while parent[y] != y:
        path.append(y)
        y = parent[y]
    r = y

    acc_len = 0
    acc_val = 0
    
    for i in range(len(path)-1,-1,-1):
        v = path[i]
        if acc_len != 0:
            dp_len[v] += acc_len
            dp_val[v] = (dp_val[v] * pow10[acc_len] + acc_val) % MOD
        acc_len = dp_len[v]
        acc_val = dp_val[v]
        parent[v] = r
        
    return r

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def getv(x):
    r = find(x)
    if r == x:
        return dp_len[x],dp_val[x]
    return dp_len[x]+dp_len[r],(dp_val[x] * pow10[dp_len[r]] + dp_val[r]) % MOD

pow10 = [1 for i in range(n+1)]
for i in range(1,n+1):
    pow10[i] = (pow10[i-1] * 10) % MOD

dp_len = [0 for i in range(size)]
dp_val = [0 for i in range(size)]



next = n
for i in range(1,m+1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1

    ra = find(a)
    rb = find(b)
    if ra == rb:
        continue

    la,va = getv(a)
    lb,vb = getv(b)

    dp_len[ra] += 1+lb
    dp_val[ra] = ((dp_val[ra] * 10 + i) * pow10[lb] + vb) % MOD

    dp_len[rb] += 1+la
    dp_val[rb] = ((dp_val[rb] * 10 + i) * pow10[la] + va) % MOD

    parent[ra] = next
    parent[rb] = next
    parent[next] = next
    next += 1

for i in range(n):
    print(getv(i)[1])