n = int(input())
arr=  list(map(int,input().split()))
arr.sort()
left = 0
right = len(arr)-1

ans = 1e10

while(left<right):
    t = arr[left]+arr[right]
    if abs(t)<ans:
        ans = abs(t)
        pr1 = arr[left]
        pr2 = arr[right]
    elif t<0:
        left+=1
    else:
        right-=1
print(min(pr1,pr2),max(pr1,pr2))