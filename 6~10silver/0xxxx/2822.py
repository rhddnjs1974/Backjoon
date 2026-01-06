arr =[]
for i in range(1,9):
    a = int(input())
    arr.append((a,i))

arr.sort()
ans = []
ansa = 0
for i in range(3,8):
    ansa+=arr[i][0]
    ans.append(arr[i][1])

ans.sort()
print(ansa)
print(*ans)