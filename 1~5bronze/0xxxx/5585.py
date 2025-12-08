n = int(input())

n = 1000 - n

ans = 0

arr = [500,100,50,10,5,1]

for i in arr:
    if n==0:
        break

    ans += n//i
    n %= i

print(ans)