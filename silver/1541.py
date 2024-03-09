import sys
input = sys.stdin.readline

arr = input().split("-")
arr3=[]
for i in arr:
    x=0
    arr2 = i.split("+")
    for j in arr2:
        x+=int(j)
    arr3.append(x)
ans=0
for i in range(len(arr3)):
    if i==0:
        ans+=arr3[i]
    else:
        ans-=arr3[i]
print(ans)