from random import randrange
import sys

input = sys.stdin.readline
import math

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

def factorial(k):
    if k==1 or k==0: return 1
    return k*factorial(k-1)

t = int(input())
for _ in range(t):
    n = int(input())
    nn = n
    ans = {}
    t = 0
    flag = 0
    while (n != 1):
        factor = rho(n)
        if factor in ans:
            ans[factor] +=1
            flag = 1
        else:
            ans[factor] = 1
            t+=1
        n //= factor

    if flag==1:
        if nn==4:
            print(1)
        else:
            print(-1)
    else:
        print(factorial(t))