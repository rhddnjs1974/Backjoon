n, k = map(int,input().split())

dong = []
for i in range(n):
    dong.append(int(input()))

ans = 0
dong.reverse()
for i in dong:
    ans+= k//i
    k %= i

    if k==0:
        break
print(ans)