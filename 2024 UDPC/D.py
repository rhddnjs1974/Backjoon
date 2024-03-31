import sys
input = sys.stdin.readline

N = int(input())
arr= list(map(int,input().split()))
ma=0
dic = {}
for i in range(N):
    while(arr[i]%2==0):
        arr[i] = arr[i]//2
    if arr[i] in dic:
        dic[arr[i]]+=1

    else:
        dic[arr[i]] = 1
    ma = max(ma, dic[arr[i]])
print(ma)