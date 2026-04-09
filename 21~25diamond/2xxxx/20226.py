from random import randrange
import sys

input = sys.stdin.readline
import math
import itertools
import bisect

prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]


# n < 3,317,011,064,679,887,385,961,981
def power(a, b, c):
    if b == 1:
        return a
    if b == 0:
        return 1
    if b % 2 == 0:
        return power(a, b // 2, c) ** 2 % c
    else:
        return a * (power(a, b // 2, c) ** 2) % c


def miller_rabin(n, a):
    r = 0
    d = n - 1
    while (d % 2 == 0):
        r += 1
        d //= 2

    x = power(a, d, n)
    if x == 1 or x + 1 == n:
        return 1

    for i in range(0, r - 1):
        x = power(x, 2, n)
        if x + 1 == n:
            return 1

    return 0


def isprime(n):
    if n in prime:
        return 1
    if n == 1 or n % 2 == 0:
        return 0
    for p in prime:
        if not miller_rabin(n, p):
            return 0
    return 1


################### v 폴라드 로 v ###################
def rho(n):
    if isprime(n):
        return n
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2
    x = randrange(2, n)
    c = randrange(1, n)
    d = 1
    y = x
    while d == 1:
        x = ((x ** 2 % n) + c) % n
        y = ((y ** 2 % n) + c) % n
        y = ((y ** 2 % n) + c) % n
        d = math.gcd(n, abs(x - y))
        if d == n:
            return rho(n)

    if isprime(d):
        return d
    else:
        return rho(d)

def makeyak(index,now):
    global yak,ans
    if index==len(ans):
        yak.add(now)
        return
    
    t = 1
    for i in range(0,ans[typeans[index]]+1):
        makeyak(index+1,now*t)
        t *= typeans[index]


while(True):
    n = int(input())
    nn=n
    if n==0:
        break
    if n==1:
        print(3)
        continue
    ans = {}
    typeans = []
    while (n != 1):
        factor = rho(n)
        if factor in ans:
            ans[factor] +=1
        else:
            ans[factor] = 1
            typeans.append(factor)
        n //= factor

    
    yak = set()
    makeyak(0,1)
    yak = list(yak)
    yak.sort()
    
    
    ans = 1e16
    for d in yak:
        m = nn//d
        x = int(m**0.5)
        index = bisect.bisect_left(yak,x+1)-1
        while(m%yak[index] !=0):
            index -=1
        i = yak[index]
        
        if ans>d+i+(m//i):
            ans = d+i+(m//i)
            xx = d
            yy = i
            zz = m//i
            hh = x
            qq = m

    print(ans)