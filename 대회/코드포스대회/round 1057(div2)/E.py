import sys
input = sys.stdin.readline
import math

def primeList(n):
    n+=1
    arr = [0,0] + [1]*n

    for i in range(2,int(n**0.5)+1):
        if arr[i]==1:
            for j in range(i*i,n+1,i):
                arr[j] = 0

    return arr

def vp(a,b):
    s=0
    while(a>0):
        a //= b
        s+=a
    return s

X = primeList(10000000)
PL = []
pi = [0]
for i in range(1,10000001):
    if X[i]==1:
        PL.append(i)
        pi.append(pi[-1]+1)
    else:
        pi.append(pi[-1])

for _ in range(int(input())):
    n,m = map(int,input().split())
    p = n #n이하 최대 소수
    while(True):
        if X[p]==1:
            break
        p-=1
    ans = 0
    for x in range(p,n):
        bfp = 10**18
        
        flag=0
        for t in PL:
            if t*t>m:
                break
            A = vp(x,t)
            B = vp(n,t)
            if B<=A:
                continue
            e = 0
            pw = 1
            while pw * t <= m:
                pw *= t
                e += 1
            Em = min(e, B)
            for e in range(2,Em+1):
                a = A//e
                b = B//e
                if b>= a+1:
                    if a<bfp:
                        bfp = a
                        if bfp ==0:
                            break
            if bfp ==0:
                break
        
        if bfp==0:
            continue
        
        for t in range(1,10000001):
            if pi[n//(t+1)] - pi[x//(t+1)] >= 1:
                break
        ans+= min(bfp,t)
    print(ans)