import sys
input = sys.stdin.readline

def primeList(n):
    n+=1
    arr = [0,0] + [1]*n

    for i in range(2,int(n**0.5)+1):
        if arr[i]==1:
            for j in range(i*2,n+1,i):
                arr[j] = 0

    return arr

x = primeList(1000000)

T = int(input())
for i in range(T):
    n = int(input())
    ans = 0
    for i in range(1+n//2):
        if x[i]==x[n-i]==1:
            ans+=1
    print(ans)