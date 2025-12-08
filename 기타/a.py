n = int(input())
arr = list(map(int,input().split()))
arr2 = list(set(arr))
idx = [i for i in range(len(arr2))]

arr2.sort()

dic = {}
for i in range(len(arr2)):
    dic[arr2[i]] = idx[i]
print(dic)

for i in arr:
    print(dic[i],end=" ")