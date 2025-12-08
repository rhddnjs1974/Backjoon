import sys
sys.setrecursionlimit(10**5)
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


n,m,a = map(int,input().split())
h = int(input())

print(power(m,n-1))

