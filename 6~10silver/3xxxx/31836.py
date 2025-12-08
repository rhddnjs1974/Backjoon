
n = int(input())
arr1 = []
arr2 = []

while(n>2):
    arr1.append(n)
    arr2.append(n-1)
    arr2.append(n-2)
    n-=3

if n==2:
    arr1.append(1)
    arr2.append(2)


print(len(arr1))
print(*arr1)
print(len(arr2))
print(*arr2)