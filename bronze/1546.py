n = int(input())
arr = list(map(int,input().split()))
ma = max(arr)
for i in range(n):
    arr[i] = arr[i]*100/ma

print(sum(arr)/n)