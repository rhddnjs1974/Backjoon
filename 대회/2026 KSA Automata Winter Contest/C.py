import sys
import math
input = sys.stdin.readline

arr = input().rstrip()
l = len(arr)
now = l-1

if l%3==0:
    need="A"
elif l%3==1:
    need="K"
else:
    need="S"

find = 0

while(now>=0):
    if arr[now]==need:
        find+=1
        l-=1
        if l%3==0:
            need="A"
        elif l%3==1:
            need="K"
        else:
            need="S"
        now-=1
    else:
        now-=2

print((len(arr)-find)*2)