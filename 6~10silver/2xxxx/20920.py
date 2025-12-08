import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = []
dic = {}
for a in range(N):
    i = input().rstrip()
    if len(i)<M:
        continue
    if i not in dic:
        dic[i] = len(arr)
        arr.append([i,1])
    else:
        arr[dic[i]][1]+=1

arr.sort()
arr.sort(key=lambda x : (-x[1],-len(x[0])))


for i,j in arr:
    print(i)