import sys
input = sys.stdin.readline
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

n,k = map(int,input().split())

A = factorial(n) #분자
B = factorial(k)*factorial(n-k) #분모

ans = (A*power(B,c-2))%c
print(ans)