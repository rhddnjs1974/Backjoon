import sys
input = sys.stdin.readline
import math
########################################
c = 1000000007
def power(a,b):
    global c
    if b==1:
        return a
    if b==0:
        return 1

    if b%2==0:
        return power(a,b//2)**2 % c
    else:
        return a*(power(a, b // 2) ** 2) % c

def factorial(a):
    global c
    n = 1
    for i in range(1,a+1):
        n*=i
        n%=c
    return n

m = int(input())
S = []
N = []

for i in range(m):
    n,s = map(int,input().split())
    N.append(n)
    S.append(s)

B = math.lcm(*N)

A = 0
for i in range(m):
    A+= (S[i]*B//N[i])


ans = (A*power(B,c-2) )%c
print(ans)