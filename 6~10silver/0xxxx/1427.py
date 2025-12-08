import sys
input = sys.stdin.readline

n = input()
arr = []
for i in n:
    arr.append(i)
arr.sort()
arr.reverse()
for i in arr:
    print(i,end="")