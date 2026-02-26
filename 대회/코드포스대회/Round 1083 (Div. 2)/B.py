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

x = primeList(100000)


for testcase in range(int(input())):
    n = int(input())
    ans = 1
    
    for i in range(100000):
        if x[i]==0:
            continue
        
        if n%i==0:
            while(n%i==0):
                n //= i
            ans *= i
    
    print(ans*n)