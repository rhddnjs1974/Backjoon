n = int(input())
arr=  list(map(int,input().split()))
x = int(input())
ans = 0
arr.sort()
left = 0
right = len(arr)-1
while(left<right):
    t = arr[left]+arr[right]

    if t==x:
        ans+=1
        left+=1
        right-=1

    elif t<x:
        left+=1
    else:
        right-=1
print(ans)