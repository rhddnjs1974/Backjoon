n = int(input())
arr1 = []
arr2 = []
for i in range(n):
    a,b = map(int,input().split())
    if a<=b:
        arr1.append((a,b))
    else:
        arr2.append((a,b))

arr1.sort()
arr2.sort(key=lambda x:(-x[1]))

ans = 1
now = 0
for i,j in arr1:
    if now<i:
        ans=0
        break
    
    now += (j-i)

for i,j in arr2:
    if now<i:
        ans=0
        break
    
    now += (j-i)

print(ans)