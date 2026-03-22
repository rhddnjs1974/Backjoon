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


print(sum1)
print(sum2)

i = 0 #sum1
j = n*n-1 #sum2

ans = 0
while(i<n*n and j>-1):
    x = sum1[i] + sum2[j]
    if x==0:
        ii = i
        jj = j
        while(ii<n*n):
            if sum1[ii]!=sum1[i]:
                break
            ii+=1
            
        while(jj>-1):
            if sum2[jj]!=sum2[j]:
                break
            jj-=1
            
        ans+= (ii-i)*(j-jj)
        
        i = ii
        j = jj
    elif x>0:
        j-=1
    else:
        i+=1
print(ans)