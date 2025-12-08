def fib(n):
    global x

    if n==1 or n==2:
        x += 1
        return 1
    return fib(n-1)+fib(n-2)

def fibonacci(n):
    global y
    for i in range(3,n+1):
        y+=1
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n]

n = int(input())
x=0
y=0
arr = [0]*(n+1)
arr[1] = 1
arr[2] = 1

fib(n)
fibonacci(n)
print(x,y)