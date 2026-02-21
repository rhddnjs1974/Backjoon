import sys
import math
input = sys.stdin.readline


n,m = map(int,input().split())

if n==1:
    ans = []
    arr = input().rstrip()
    i=0
    while(i<m):
        if arr[i] == "X":
            if i!=m-1 and arr[i+1]=="X":
                ans.append((2,i+1,i+2))
                i+=1
            else:
                ans.append((1,i+1))
        i+=1
    
    print(len(ans))
        
    for i in ans:
        print(*i)
else:
    arr = []
    ans = []

    for i in range(n):
        arr.append([])
        arr[-1] = (input().rstrip())

    for i in range(m):
        j=0
        while(j<n):
            if arr[j][i] == "X":
                if j!=n-1 and arr[j+1][i]=="X":
                    ans.append((2,1+i*n+j,2+i*n+j))
                    j+=1
                else:
                    ans.append((1,1+i*n+j))
            j+=1
    print(len(ans))
    for i in ans:
        print(*i)