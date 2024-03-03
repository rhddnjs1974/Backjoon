s = input()
point = -1

arr = [-1]*26

for i in s:
    point+=1
    if arr[ord(i)-97]==-1:
        arr[ord(i) - 97]=point

print(*arr)