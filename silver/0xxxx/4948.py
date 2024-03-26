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

x = primeList(250001)

array = [0]*250001

for i in range(1,250000):
    array[i] = array[i-1]+x[i]


while(True):
    N = int(input())
    if N==0:
        break
    print(array[N*2]-array[N])