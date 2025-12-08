import sys
input = sys.stdin.readline
import sys

N = int(input())
C = list(map(int,input().split()))
X = list(map(int,input().split()))

cost = 0
for i in C:
    cost += X[i-1]+1

C = C+C

candis = []

for i in range(N):
    x = X[C[i]-1]+1
    for j in range(1,x):
        k = i+j
        if C[i]==C[k]:
            candis.append((i,i+j,x-j,C[i]))

candis.sort(key = lambda x : x[3])
T = len(candis)
plus = []
for i in range(T-1):
    if candis[i][1]==candis[i+1][0] and candis[i][3]==candis[i+1][3]:
        plus.append((candis[i][0],candis[i+1][1],candis[i][2]+candis[i+1][2]+X[candis[i][3]-1]-2 ,candis[i][3]))        

for j in plus:
    candis.append(j)

ansdis = 0
print(candis)
def bt(n,arr,discount):
    global ansdis,N
    if n==len(candis):
        ansdis = max(ansdis,discount)
        return
    x,y,z,w = candis[n]
    x %= N
    y %= N
    if arr[x]==0 and arr[y]==0:
        arr[x]=1
        arr[y]=1
        bt(n+1,arr,discount+z)
        arr[x]=0
        arr[y]=0
    bt(n+1,arr,discount)
    

arr = [0]*N
bt(0,arr,0)
print(cost-ansdis)