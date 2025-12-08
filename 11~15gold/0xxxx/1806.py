n,s = map(int,input().split())
arr=  list(map(int,input().split()))

ans = 100001

left = 0
right = 0
t = arr[0]

while(True):

    if t<s:
        right+=1
        if right==n:
            break
        t+=arr[right]
    else:
        if right - left < ans:
            ans = right - left

        t-=arr[left]
        left+=1



if ans==100001:
    print(0)
else:
    print(ans+1)