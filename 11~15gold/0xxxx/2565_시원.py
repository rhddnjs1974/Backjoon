import sys
import math
from collections import deque
input = sys.stdin.readline

x = int(input())
# list [시작, 끝, 지나가는 전깃줄의 시작번호]
arr= [[i,0, []] for i in range(501)]
for i in range(x):
    a,b = map(int, input().split())
    arr[a][1] = b
    for j in range(1,len(arr)):
        if arr[j][1] == 0:
            continue
        if j<a and arr[j][1] > b:
            arr[j][2].append(a)
            arr[a][2].append(j)
        if j>a and arr[j][1] < b:
            arr[j][2].append(a)
            arr[a][2].append(j)

# 연결된 전기줄이 없으면 삭제
for i in range(500,-1, -1):
    if arr[i][1] == 0:
        arr.pop(i)

arr= sorted(arr, key= lambda x: (len(x[2]),-x[0]))


for i in range(len(arr)-1,-1,-1):
    if len(arr[i][2]) == 0:
        arr.remove(arr[i])

count = 0
while len(arr) > 0:
    count+=1
    t = arr.pop()
    
    for i in arr:
        if i[0] in t[2]:
            i[2].remove(t[0])

    arr= sorted(arr, key= lambda x: (len(x[2]),-x[0]))

    for i in range(len(arr)-1,-1,-1):
        if len(arr[i][2]) == 0:
            arr.remove(arr[i])

print(count)

"""
10
1 6
2 8
3 2
4 9
5 5
6 10
7 4
8 1
9 7
10 3
"""