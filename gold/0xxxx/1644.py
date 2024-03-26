import sys
input = sys.stdin.readline

def primeList(n):
    n+=1
    arr = [0,0] + [1]*n

    for i in range(2,int(n**0.5)+1):
        if arr[i]==1:
            for j in range(i*2,n+1,i):
                arr[j] = 0

    return arr

x = primeList(4000000)
arr = []
for i in range(4000001):
    if x[i]==1:
        arr.append(i)

n = int(input())

ans = 0

left = 0
right = 0
t = arr[0]

l = len(arr)

while(True):

    if t==n:
        ans+=1
        t -= arr[left]
        left+=1
        right+=1
        if right == l:
            break
        t += arr[right]

    elif t<n:
        right+=1
        if right == l:
            break
        t+=arr[right]
    else:
        t-=arr[left]
        left+=1




print(ans)