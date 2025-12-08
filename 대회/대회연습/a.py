import sys
input = sys.stdin.readline

s = input().rstrip()
arr = []


for i in range(len(s)):
    arr.append("")
    for j in range(i,len(s)):
        arr[i] += s[j]

arr.sort()
for i in arr:
    print(i)