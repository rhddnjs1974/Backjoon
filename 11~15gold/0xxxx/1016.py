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

a,b = map(int,input().split())

t = primeList(1000000)

array = [1]*(b-a+1)
for i in range(1000000):
    if t[i]==1:
        i = i*i
        x = (a//i)*i
        if x<a:
            x+=i

        while(x<=b):
            array[x-a]=0
            x+=i
print(sum(array))

