a,b = map(int,input().split())
man = a*b
arr = list(map(int,input().split()))
for i in range(5):
    arr[i] -= man
print(*arr)