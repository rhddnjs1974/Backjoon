import sys
input = sys.stdin.readline

n,m = map(int,input().split())

ans = 0
for i in range(0,m+1):
    ans += n**i
    if ans>1e9:
        break

if ans>1e9:
    print("inf")
else:
    print(ans)