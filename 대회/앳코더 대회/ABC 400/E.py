import sys
input = sys.stdin.readline
import bisect

def primeList(n):
    n+=1
    arr = [0,0] + [1]*n

    for i in range(2,int(n**0.5)+1):
        if arr[i]==1:
            for j in range(i*2,n+1,i):
                arr[j] = 0

    pl = []
    for i in range(n):
        if arr[i]==1:
            pl.append(i)
    return pl

PL = primeList(1000001)
s400 = set()

for i in range(len(PL)):
    p = PL[i]
    p2 = p*p

    while p2<=1e12:
        for j in range(i+1,len(PL)):
            q = PL[j]
            q2 = q*q
            if p2*q2>1e12:
                break
            while p2*q2<=1e12:
                s400.add(p2*q2)
                q2 *= q*q
        p2 *= p*p

s400 = list(s400)
s400.sort()

Q = int(input())

for _ in range(Q):
    x = int(input())
    point = bisect.bisect_left(s400,x+1)
    print(s400[point-1])