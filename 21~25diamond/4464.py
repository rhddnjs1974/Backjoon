from random import randrange
import sys
import bisect
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
    
def makeyak(index,now):
    global yak,ans
    if index==len(ans):
        yak.add(now)
        return
    
    t = 1
    for i in range(0,ans[typeans[index]]+1):
        makeyak(index+1,now*t)
        t *= typeans[index]

def vam(x):
    x = str(x)
    f = 0
    for i in x:
        if i=="0":
            if f==1:
                return False
            f=1
        else:
            f=0
    return True

  
while(True):
    n = int(input())
    nn=n
    if n==0:
        break
    if len(str(n))%2!=0:
        print(n,end=": no\n")
        continue
    
    dic = {}
    for i in str(n):
        if i in dic:
            dic[i]+=1
        else:
            dic[i] = 1
    
    
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
    
    t = 10**(len(str(nn))//2)
    mit = t//10
    
    index = bisect.bisect_left(yak,t)
    flag=0
    
    
    while(yak[index]>=mit and index>=0):
        a = yak[index]
        if mit<=a<t:
            if not vam(a):
                index -=1
                continue
            b = nn//a
            if not vam(b):
                index -=1
                continue
            if mit<=b<t:
                if a%10==0 and b%10==0:
                    index -=1
                    continue
                
                dic2 = {}
                xx = str(a)+str(b)
                for yy in xx:
                    if yy in dic2:
                        dic2[yy] +=1
                    else:
                        dic2[yy] = 1
                
                flag2 = 0
                for xxx in dic:
                    if xxx not in dic2:
                        flag2=1
                        break
                    if xxx in dic2 and dic[xxx]!=dic2[xxx]:
                        flag2=1
                        break
                if flag2==1:
                    index-=1
                    continue
                
                flag=1
                break
        index -=1
    
    if flag==1:
        print(nn,end=": yes\n")
    else:
        print(nn,end=": no\n")
        