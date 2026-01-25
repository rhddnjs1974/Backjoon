import sys
input = sys.stdin.readline

q = int(input())

play = 0
v = 0

for i in range(q):
    a = int(input())
    if a==1:
        v+=1
    elif a==2:
        if v>0:
            v-=1
    elif a==3:
        play = 1-play

    if play==1 and v>=3:
        print("Yes")
    else:
        print("No")