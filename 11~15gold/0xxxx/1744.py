n = int(input())
arr = []
arr2 = []
ans = 0
for _ in range(n):
    x = int(input())
    if x>0:
        if x==1:
            ans+=1
            continue
        arr.append(x)
    else:
        arr2.append(x)
arr.sort()
arr2.sort()
arr2.reverse()



while(arr):
    a = arr.pop()
    if len(arr)==0:
        ans+=a
        break
    b = arr.pop()
    ans+= (a*b)

while(arr2):
    a = arr2.pop()
    if len(arr2)==0:
        ans+=a
        break
    b = arr2.pop()
    ans+= (a*b)
print(ans)