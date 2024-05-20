import sys
input = sys.stdin.readline

def phi(n):
    N = n
    for i in range(2,1+N):
        if i*i>N:
            break
        if N%i==0:
            n = n/ i *(i-1)
            while(N%i==0):
                N=N//i
    if N>1:
        n = n / N * (N-1)
    return int(n)


n = int(input())

flag = 0
for i in range(1,n+1):
    if i*i>n:
        break
    if n%i!=0:
        continue
    m = n//i
    if phi(i)==m:
        print(i)
        flag = 1
        break

    m = n//m
    if phi(n//i)==m:
        print(n//i)
        flag = 1
        break

if flag==0:
    print(-1)
