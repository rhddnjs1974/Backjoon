import sys
input = sys.stdin.readline

N, K = map(int,input().split())
S = []

S.append(input().rstrip())
S.append(input().rstrip())


if S[0][0]==".":
    csu = 1
else:
    csu = 0
if S[1][0]==".":
    csd = 1
else:
    csd = 0
if S[0][-1] == ".":
    ceu = 1
else:
    ceu = 0
if S[1][-1] == ".":
    ced = 1
else:
    ced = 0

flag= 0
UU=1e15
UD=1e15
DD=1e15
DU=1e15


if csu==1:
    t = N - 1
    now = 0 # 0 : u 1 : d
    for i in range(0,N-1):
        if S[now][i+1]=="#":
            if S[1-now][i]=="#":
                flag=1
                break
            else:
                now = 1-now
                t+=1
    if flag==0:
        if now==0:
            UU = t
            if ced==1:
                UD = t+1
        else:
            UD=t
            if ceu==1:
                UU = t+1


if csd==1:
    t = N - 1
    now = 1 # 0 : u 1 : d
    for i in range(0,N-1):
        if S[now][i+1]=="#":
            if S[1-now][i]=="#":
                flag=1
                break
            else:
                now = 1-now
                t+=1
    if flag==0:
        if now==0:
            DU = t
            if ced==1:
                DD = t+1
        else:
            DD=t
            if ceu==1:
                DU = t+1

ans = -100

if flag==1:
    print(-1)
else:
        if csu and csd:
            ans = (1+min(UU,UD,DU,DD))*(K-1)
        elif csu:
            ans = (1+min(UU,DU))*(K-1)
        elif csd:
            ans = (1+min(UD,DD))*(K-1)


        if ans==-100 or ans>=1e15:
            print(-1)
        else:
            print(int(ans+min(UU,UD,DU,DD)))