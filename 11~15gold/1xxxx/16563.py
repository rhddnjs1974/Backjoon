
def primeList(n):
    n+=1
    arr = [0,0] + [1]*n

    for i in range(2,int(n**0.5)+1):
        if arr[i]==1:
            for j in range(i*2,n+1,i):
                arr[j] = i

    return arr

x = primeList(5000000)

n = int(input())
arr = list(map(int,input().split()))

for i in arr:
    ans = []
    a = i
    while(True):
        t = x[a]
        if t==1:
            break
        a //= t
        ans.append(t)
    ans.append(a)
    ans.sort()
    print(*ans)