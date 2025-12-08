import sys
input = sys.stdin.readline
from collections import deque

def cross(A,B,C,D):
    p = ccw(*A, *B, *C) * ccw(*A, *B, *D)
    q = ccw(*C, *D, *A) * ccw(*C, *D, *B)

    if p <= 0 and q <= 0:
        if p == 0 and q == 0:
            if min(A[0], B[0]) <= max(C[0], D[0]) and min(C[0], D[0]) <= max(A[0], B[0]) and min(A[1], B[1]) <= max(
                    C[1], D[1]) and min(C[1], D[1]) <= max(A[1], B[1]):
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0


def ccw(x1,y1,x2,y2,x3,y3):
    c = (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
    return c

def inside(shape,dot):
    a,b = dot
    C = [a,b]
    D = [1000000001,b+1] #최대x +1,해당y+1
    t=0
    for j in range(len(shape)):
        A=shape[j]
        B=shape[(j+1)%len(shape)]
        t+= cross(A,B,C,D)
        if cross(A,B,C,C)==1:
            t=1
            break
        if A[0]==C[0] and A[1]==C[1]:
            t=1
            break
    return t%2
    
n,C = map(int,input().split())
arr = []
dic = {}
q = deque()
for i in range(n):
    a,b,c,d = map(int,input().split())
    f=0
    for j in dic:
        if dic[j]==(a,b):
            arr[j].append((c,d))
            dic[j]=(c,d)
            f = 1
            break
        if dic[j]==(c,d):
            arr[j].append((a,b))
            dic[j]=(a,b)
            f=1
            break
    if f==0:
        arr.append([])
        arr[-1].append((a,b))
        arr[-1].append((c,d))
        dic[len(arr)-1]=(c,d)

live = [1]*len(arr)

while(True):
    if sum(live)==0:
        break
    for i in range(len(live)):
        if live[i]==0:
            continue
        if arr[i][0]==arr[i][-1]:
            live[i]=0
            continue
        for j in range(len(live)):
            if j==i or live[j]==0:
                continue
            if arr[i][-1]==arr[j][0]:
                for t in arr[j][1:]:
                    arr[i].append(t)
                live[j]=0
                arr[j] = 0
                break
            if arr[i][-1]==arr[j][-1]:
                arr[j].reverse()
                for t in arr[j][1:]:
                    arr[i].append(t)
                live[j]=0
                arr[j] = 0
                break

realarr = []
for i in arr:
    if i!=0:
        realarr.append(i)

cow = []
for i in range(C):
    a,b = map(int,input().split())
    cow.append((a,b))

insidearr = [[] for i in range(len(realarr))]
for x in range(len(realarr)):
    for j in range(C):
        if inside(realarr[x],cow[j]):
            insidearr[x].append(j)


dp = [0]*C
for i in range(len(realarr)):
    for x in insidearr[i]:
        dp[x]+=(1<<i)

dic = {}
for x in dp:
    if x in dic:
        dic[x]+=1
    else:
        dic[x]=1
        
ma=0
for x in dic:
    ma=max(ma,dic[x])
print(ma)