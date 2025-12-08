import math
import sys
input = sys.stdin.readline
pi = math.pi
x1, y1, r1, x2, y2, r2  = map(float, input().split())
d = math.sqrt(pow(x2-x1,2) + pow(y2-y1,2))

if (d > r2 + r1):
    print("0.000") #<<<<<<<<<<<<<<<<이게 94퍼 오답의 원인
elif (d <= abs(r1-r2) and r1<r2):
    ans = pi * r1*r1
    ans = float(round(1000*ans)/1000)
    print('%.3f' % ans)
elif (d <= abs(r1-r2) and r1>=r2):
    ans = pi * r2*r2
    ans = float(round(1000 * ans) / 1000)
    print('%.3f' % ans)
else:
    theta1 = (math.acos(((r1*r1) + (d * d) - (r2*r2)) / (2 * r1 * d))) * 2
    theta2 = (math.acos(((r2*r2) + (d * d) - (r1*r1)) / (2 * r2 * d))) * 2
    ans1 = 0.5 * r2*r2 * (theta2 - math.sin(theta2))
    ans2 = 0.5 * r1*r1 * (theta1 - math.sin(theta1))
    ans = ans1+ans2

    ans = float(round(1000 * (ans)) / 1000)
    
    print('%.3f' % ans)
