import sys
input = sys.stdin.readline

N = int(input())
dist = list(map(int,input().split()))
oil_price = list(map(int,input().split()))

cheap = 1e10
ans=0
for i in range(N-1):
    cheap = min(cheap,oil_price[i])
    ans+=dist[i]*cheap

print(ans)