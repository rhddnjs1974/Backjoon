import sys
input = sys.stdin.readline

n = int(input())
arr = [0]*10
add = 0

i = 1
while(n!=0):
    cur = n%10
    n //= 10
    
    arr[0] -= i
    for j in range(cur):
        arr[j] += (n+1)*i
    arr[cur] += (n*i+1+add)
    for j in range(cur+1,10):
        arr[j] += n*i
    
    add += cur*i
    
    i*=10

print(*arr)