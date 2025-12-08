n = int(input())
arr =[]
arr2=[]
for i in range(n):
    arr.append(input())

for i in range(n):
    arr2.append(input())
ans = 0
for i in range(n):
    if arr[i]==arr2[i]:
        ans+=1
print(ans)