import sys
input = sys.stdin.readline

n = int(input())
k = (n-1)//2
m = n-1

for i in range(k):
    arr = [n, i+1]
    
    for d in range(1, k):
        arr.append(((i-d)%m)+1)
        arr.append(((i+d)%m)+1)
        
    arr.append(((i-k)%m)+1)

    for j in range(n):
        print(arr[j], end=' ')
    print()