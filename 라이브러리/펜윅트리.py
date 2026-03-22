def update(i,dif):
    while(i<=n):
        fenwick[i] += dif
        i += (i & -i)

def subsum(i):
    ans = 0
    while(i>0):
        ans += fenwick[i]
        i -= (i & -i)
    return ans

n,m,k = map(int,input().split())

fenwick = [0]*(n+1)
now = [0]*(n+1)

for i in range(1,n+1):
    x = int(input())
    update(i,x)
    now[i] = x

for i in range(m+k):
    a,b,c = map(int,input().split())
    if a==1:
        update(b,c-now[b])
        now[b] = c
    else:
        print(subsum(c)-subsum(b-1))