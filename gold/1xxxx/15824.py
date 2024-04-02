import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
########################################
c = 1000000007
a = [0]
for i in range(300000):
    a.append((1+a[i]*2)%c)

n = int(input())
arr= list(map(int,input().split()))
arr.sort()
ans = 0
for i in range(n):
    ans-= a[i]*(arr[n-i-1]-arr[i])
    ans %= c
print(ans)