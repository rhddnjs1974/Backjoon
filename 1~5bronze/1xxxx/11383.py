n, m = map(int,input().split())
arr = []
arr2 = []
arr3 = []

for i in range(n):
    arr.append(input())
for i in range(n):
    arr2.append(input())

flag = 0

for i in range(n):
    x = ""
    for j in arr[i]:
        x += j*2
    arr3.append(x)

for i in range(n):
    if arr2[i]!=arr3[i]:
        flag=1
        break

if flag==1:
    print("Not Eyfa")
else:
    print("Eyfa")