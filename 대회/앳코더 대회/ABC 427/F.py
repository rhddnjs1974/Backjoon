import sys
input = sys.stdin.readline
from collections import Counter

N,M = map(int,input().split())
A = list(map(int,input().split()))

def dfsl(i,pre,sum,lastt):
    global M
    if i==len(L):
        if lastt:
            l1.append(sum)
        else:
            l0.append(sum)
        return
    dfsl(i+1,0,sum,lastt)
    if pre==0:
        sum = (sum+L[i])%M
        if i==len(L)-1:
            lastt=1
        dfsl(i+1,1,sum,lastt)

def dfsr(i,pre,sum,firstt):
    global M
    if i==len(R):
        if firstt:
            r1.append(sum)
        else:
            r0.append(sum)
        return
    dfsr(i+1,0,sum,firstt)
    if pre==0:
        sum = (sum+R[i])%M
        if i==0:
            firstt=1
        dfsr(i+1,1,sum,firstt)

l0 = []
l1 = []
r0 = []
r1 = []
L = A[:N//2]
R = A[N//2:]

dfsl(0,0,0,0)
dfsr(0,0,0,0)


cr0 = Counter(r0)
cr1 = Counter(r1)
ans = 0


for i in l0:
    ans += cr0[(-i)%M]
    ans += cr1[(-i)%M]
for i in l1:
    ans += cr0[(-i)%M]
print(ans)