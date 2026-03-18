A,B,C = map(int,input().split())

dic1 = {}
dic2 = {}

for i in range(A):
    x,y = input().split()
    y = int(y)
    dic1[x] = y
for i in range(B):
    x,y = input().split()
    y = int(y)
    dic2[x] = y
for i in range(C):
    a = input()

N = int(input())
now1 = 0
now = 0
spe = 0
sur = 0
for i in range(N):
    a = input()
    if a in dic1:
        now += dic1[a]
        now1 += dic1[a]
    elif a in dic2:
        spe += 1
        now += dic2[a]
    else:
        sur += 1

if sur>1:
    print("No")
elif sur==1 and now<50000:
    print("No")
elif spe>0 and now1<20000:
    print("No")
else:
    print("Okay")