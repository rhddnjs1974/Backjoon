import sys
input = sys.stdin.readline

N = int(input())

dic = {}

arr = []
for i in range(N):
    arr.append(int(input()))

x = sum(arr)
print(round(x/N))


arr.sort()

print(arr[N//2])

ma= 0
for i in arr:
    if i not in dic:
        dic[i]= 1
    else:
        dic[i] +=1
    ma = max(ma,dic[i])

ans = []

for i in arr:
    if dic[i]==ma:
        if i not in ans:
            ans.append(i)


if len(ans)>1:
    ans.sort()
    print(ans[1])
else:
    print(ans[0])

print(arr[-1]-arr[0])