import copy
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

q = deque()
q.append((arr,0))
ma = 0
while(q):
    array,num = q.popleft()

    if num==4:
        for i in array:
            ma = max(ma,max(i))
        continue

    for i in range(4):
        narray = copy.deepcopy(array)

        if i==0:#왼쪽
            for x in range(n):
                for y in range(1,n):
                    t = narray[x][y]
                    narray[x][y] = 0
                    while(y-1>=0 and narray[x][y-1]==0):
                        y-=1
                    if y-1>=0 and narray[x][y-1]==t:
                        narray[x][y-1]=2*t
                    else:
                        narray[x][y] = t

            q.append((narray,num+1))

        if i==1:#오른쪽

            for x in range(n):
                for y in range(n-2,-1,-1):

                    t = narray[x][y]

                    narray[x][y] = 0
                    while(y+1<n and narray[x][y+1]==0):
                        y+=1
                    if y+1<n and narray[x][y+1]==t:
                        narray[x][y+1]=2*t
                    else:
                        narray[x][y] = t

            q.append((narray,num+1))


        if i==2:#아래쪽
            for y in range(n):
                for x in range(n-2,-1,-1):


                    t = narray[x][y]

                    narray[x][y] = 0
                    while(x+1<n and narray[x+1][y]==0):
                        x+=1
                    if x+1<n and narray[x+1][y]==t:
                        narray[x+1][y]=2*t
                    else:
                        narray[x][y] = t

            q.append((narray,num+1))

        if i==3:#위쪽
            for y in range(n):
                for x in range(1,n):


                    t = narray[x][y]

                    narray[x][y] = 0
                    while(x-1>=0 and narray[x-1][y]==0):
                        x-=1
                    if x-1>=0 and narray[x-1][y]==t:
                        narray[x-1][y]=2*t
                    else:
                        narray[x][y] = t

            q.append((narray,num+1))

print(ma)