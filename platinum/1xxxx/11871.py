import sys
input = sys.stdin.readline

n = int(input())
arr= list(map(int,input().split()))

a = 0
mex = [0]*(n+1)

for i in arr:
    if i==0 or i==2:
        t = 0
    elif i==1:
        t = 1
    else:
        if i%2==1:
            t = (i+1)//2
        else:
            t = (i-2)//2

    a^=t

if a==0:
    print("cubelover")
else:
    print("koosaga")
