n = int(input())
arr = list(map(int,input().split()))
b,c = map(int,input().split())

ans = n
for i in arr:
    if i<=b:
        continue
    i-=b
    i-=1
    a = i//c
    ans+=(a+1)
print(ans)