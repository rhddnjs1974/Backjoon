import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
########################################
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

n = int(input())
c = 1000000007
ans = 0
for i in range(n):
    d, k = map(int,input().split())

    if k==0:
        ans += 0
    else:
        ans += d*k*power(2,k-1)
    ans %= c

print(ans%c)