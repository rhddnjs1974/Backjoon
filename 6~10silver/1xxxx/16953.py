import sys
input = sys.stdin.readline

a,b = map(int,input().split())
t = 0
while(True):
    if a==b:
        break
    if a>b:
        t=-1
        break
    t+=1
    if b%2==0:
        b//=2
    elif b%10==1:
        b//=10
    else:
        t=-1
        break

if t==-1:
    print(-1)
else:
    print(t+1)