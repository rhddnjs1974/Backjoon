n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()

ma = 0
for i in range(n):
    ma = max(arr[i]*(n-i),ma)
print(ma)