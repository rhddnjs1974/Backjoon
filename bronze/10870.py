def fibo(N):
    if N==0 or N==1 or N==2:
        if N==0:
            return 0
        else:
            return 1
    return fibo(N-1)+fibo(N-2)

n = int(input())
print(fibo(n))