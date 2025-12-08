mod = 1000000007
import sys
n, m = map(int,input().split())
sys.setrecursionlimit(10**5)
########################################
def power(a,b):
    global mod
    c = mod
    if b==1:
        return a
    if b==0:
        return 1

    if b%2==0:
        return power(a,b//2)**2 % c
    else:
        return a*(power(a, b // 2) ** 2) % c
    
    
def primeList(n):
    n+=1
    arr = [0,0] + [1]*n

    for i in range(2,int(n**0.5)+1):
        if arr[i]==1:
            for j in range(i*2,n+1,i):
                arr[j] = 0

    return arr

x = primeList(15000000)
ans = 1
for i in range(min(n,m)+1):
    if x[i]==1:
        c = 0
        j=i
        while(j<=min(n,m)):
            c += ((n//j)*(m//j))
            j *= i
            
        ans = (ans*power(i,c)) % mod
        
print(ans%mod)