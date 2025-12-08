n = int(input())
arrr = list(map(int,input().split()))

def primeList(n):
    n+=1
    arr = [0,0] + [1]*n


    for i in range(2,int(n**0.5)+1):
        if arr[i]==1:

            for j in range(i*2,n+1,i):
                arr[j] = 0

    return arr

x = primeList(2000000)
prime = []
for i in range(1,2000001):
    if x[i]==1:
        prime.append(i)

ans = 1
for i in prime:
    if i>2000000/ans:
        break
    dic = {}
    for j in arrr:
        if j%i in dic:
            dic[j%i] += 1
            ans = max(ans,dic[j%i])
        else:
            dic[j%i] = 1
    
print(ans)