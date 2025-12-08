import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(9):
    arr.append({})

for i in range(n):
    a = input().rstrip()
    l = len(a)
    for j in range(l):

        if a[j] in arr[l-j-1]:
            arr[l-j-1][a[j]]+=1
        else:
            arr[l-j-1][a[j]]=1
        if arr[l-j-1][a[j]]==10:
            arr[l - j - 1][a[j]] = 0
            if a[j] in arr[l - j]:
                arr[l - j][a[j]] += 1
            else:
                arr[l - j][a[j]] = 1

print(arr)