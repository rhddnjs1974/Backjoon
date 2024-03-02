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

x = primeList(1000000)

while(True):
    a = int(input())
    if a==0:
        break

    for i in range(3,a):
        if x[i]==1 and x[a-i]==1:
            print("%d = %d + %d"%(a,i,a-i))
            break