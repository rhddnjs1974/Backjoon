arr = ["a","e","i","o","u"]

n = int(input())
ans = 0
arr2= input()
for i in arr2:
    if i in arr:
        ans+=1
print(ans)