import math

def primeList(n):
    n+=1
    arr = [0,0] + [1]*n

    for i in range(2,int(n**0.5)+1):
        if arr[i]==1:
            arr[i]=i
            for j in range(i*2,n+1,i):
                if arr[j]==1:
                    arr[j] = i

    return arr

x = primeList(20000000)

for i in range(int(input())):
    a,b = map(int,input().split())
    g = math.gcd(a,b)
    if g==a or g==b:
        print(a,b)
    else:
        if a%2==0 or b%2==0:
            if g!=1:
                if x[g]==1:
                    print(a,g,b)
                else:
                    print(a,x[g],b)
            else:
                print(a,math.lcm(a,b),b)
        else:
            print(a,1,b)