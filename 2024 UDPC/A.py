import sys
input = sys.stdin.readline

C = []
D = []
for i in range(3):
    a,b = map(int,input().split())
    C.append(a)
    D.append(b)

H = int(input())

now1 = 0
now2 = 0
now3 = 0
time = -1
while(H>0):
    time+=1
    if now1==time:
        now1+=C[0]
        H-=D[0]

    if now2==time:
        now2+=C[1]
        H-=D[1]

    if now3==time:
        now3+=C[2]
        H-=D[2]

print(time)