import sys
input = sys.stdin.readline
from itertools import combinations
from bisect import bisect_left,bisect_right
####################################
n = int(input())
A=[]
B=[]
C=[]
D=[]
for i in range(n):
    a,b,c,d = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

sum1 = []
sum2 = []

for i in range(n):
    for j in range(n):
        sum1.append(A[i]+B[j])
        sum2.append(C[i]+D[j])

sum1.sort()
sum2.sort()



ans=0
for i in sum1:
    t = bisect_right(sum2,-i)
    p = bisect_left(sum2,-i)
    ans+= (t-p)

print(ans)