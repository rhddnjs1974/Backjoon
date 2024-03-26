import sys
input = sys.stdin.readline
from itertools import combinations
from bisect import bisect_left,bisect_right
####################################
n,c = map(int,input().split())
arr=  list(map(int,input().split()))

arr1 = arr[:n//2]
arr2 = arr[n//2:]

sum1 = []
sum2 = []

for i in range(len(arr1)+1):
    for j in combinations(arr1,i):
        sum1.append(sum(j))

for i in range(len(arr2)+1):
    for j in combinations(arr2,i):
        sum2.append(sum(j))

sum1.sort()
sum2.sort()


ans=0

for i in sum1:
    t = bisect_right(sum2,c-i)
    p = bisect_left(sum2,c-i)
    ans+= (t-p)

if c==0:
    ans-=1

print(ans)