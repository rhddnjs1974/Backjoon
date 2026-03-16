N = int(input())
ans = 0

arr = []


for i in range(N+1):
    if i==N:
        h = 0
    else:
        h = int(input())
    if not arr:
        arr.append([h,1])
    else:
        if arr[-1][0]<h:
            arr.append([h,1])
        else:
            count = 1
            arr2= []
            while(arr):
                x,n = arr.pop()
                if x<h:
                    arr.append([x,n])
                    break
                arr2.append([x,n])
                count+=n
            
            now = 0
            for a,b in arr2:
                now+=b
                ans = max(ans,a*now)

            
            ans = max(ans,h*count)
            arr.append([h,count])

print(ans)