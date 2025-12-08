import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr2=[]
for i in range(n):
    arr2.append((arr[i],i))
arr2.sort()
t=0
for i in range(n):
    if i>0 and arr2[i-1][0]==arr2[i][0]:
        t+=1
    arr[arr2[i][1]]=i-t
print(*arr)