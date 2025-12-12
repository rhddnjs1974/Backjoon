import math
t = list(map(float,input().split()))
t.sort()
for i in range(4):
    t[i] = round(t[i]*100)
goal = float(input())

goal = round(goal*100)

if (t[0]+t[1]+t[2]) / 3 > goal:
    print("impossible")
elif (t[1]+t[2]+t[3]) / 3 <= goal:
    print("infinite")
else:
    print("%.2f"%((3*goal-t[1]-t[2])/100))