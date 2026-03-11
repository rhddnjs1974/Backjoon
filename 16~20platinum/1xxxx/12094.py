import copy
import sys
input = sys.stdin.readline
from collections import deque


def move(narray, i):
    if i==0:#왼쪽
        for x in range(n):
            arr1=[]
            for y in range(n):
                if narray[x][y]!=0:
                    arr1.append(narray[x][y])

            arr2=[]
            y=0
            while y<len(arr1):
                if y+1<len(arr1) and arr1[y]==arr1[y+1]:
                    arr2.append(arr1[y]*2)
                    y+=2
                else:
                    arr2.append(arr1[y])
                    y+=1

            arr2 += [0]*(n-len(arr2))

            for y in range(n):
                narray[x][y]=arr2[y]
            

    if i==1:#오른쪽
        for x in range(n):
            arr1=[]
            for y in range(n-1,-1,-1):
                if narray[x][y]!=0:
                    arr1.append(narray[x][y])

            arr2=[]
            y=0
            while y<len(arr1):
                if y+1<len(arr1) and arr1[y]==arr1[y+1]:
                    arr2.append(arr1[y]*2)
                    y+=2
                else:
                    arr2.append(arr1[y])
                    y+=1

            arr2 += [0]*(n-len(arr2))

            for y in range(n):
                narray[x][n-1-y]=arr2[y]
                
    if i==2:#위쪽
        for y in range(n):
            arr1=[]
            for x in range(n-1,-1,-1):
                if narray[x][y]!=0:
                    arr1.append(narray[x][y])

            arr2=[]
            x=0
            while x<len(arr1):
                if x+1<len(arr1) and arr1[x]==arr1[x+1]:
                    arr2.append(arr1[x]*2)
                    x+=2
                else:
                    arr2.append(arr1[x])
                    x+=1

            arr2 += [0]*(n-len(arr2))

            for x in range(n):
                narray[n-1-x][y]=arr2[x]
    
    
    if i==3:#아래쪽
        for y in range(n):
            arr1=[]
            for x in range(n):
                if narray[x][y]!=0:
                    arr1.append(narray[x][y])

            arr2=[]
            x=0
            while x<len(arr1):
                if x+1<len(arr1) and arr1[x]==arr1[x+1]:
                    arr2.append(arr1[x]*2)
                    x+=2
                else:
                    arr2.append(arr1[x])
                    x+=1

            arr2 += [0]*(n-len(arr2))

            for x in range(n):
                narray[x][y]=arr2[x]
    

n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))


ma = 0
def dfs(array,num):
    global ma

    nowma = 0 
    for i in array:
        nowma = max(nowma,max(i))
        
    ma = max(ma,nowma)
    
    if num==10:
        return
    
    if nowma*(2**(10-num))<=ma:
        return
    
    for i in range(4):
        narray = [row[:] for row in array]
        move(narray,i)
        
        if array == narray:
            continue
        
        dfs(narray,num+1)

dfs(arr,0)
print(ma)

