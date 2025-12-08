import math
s, p = map(int,input().split())

def f(n):
    return math.pow((s/n),n)

if s==p:
    print(1)
else:
    now = f(1)
    flag=0
    N=1
    while(True):
        if now>=p:
            flag=1
            break
        N+=1
        now = f(N)
        if N>2 and f(N)<f(N-1):
            break
    if flag==1:
        print(max(N,2))
    else:
        print(-1)