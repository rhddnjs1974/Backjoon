N = int(input())
a = input()

bluenum = 0
rednum = 0

for i in a:
    if i=="B":
        bluenum+=1

rednum = N-bluenum

s = a[0]
LB = 0
LR = 0
RB = 0
RR = 0
if s=="B":
    for i in a:
        if i=="B":
            LB+=1
        else:
            break
else:
    for i in a:
        if i=="R":
            LR+=1
        else:
            break
b = a[::-1]
e = b[0]

if e=="B":
    for i in b:
        if i=="B":
            RB+=1
        else:
            break
else:
    for i in b:
        if i=="R":
            RR+=1
        else:
            break

print(min(bluenum-LB,bluenum-RB,rednum-LR,rednum-RR))
