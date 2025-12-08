import sys
import math
input = sys.stdin.readline

n = int(input())
py = 0
my = 0
px = 0
mx = 0
dic = {}
for _ in range(n):
    a,b = map(int,input().split())
    if a==0 or b==0:
        if a==0 and b>0:
            py+=1
        elif a==0 and b<0:
            my+=1
        elif b==0 and a>0:
            px+=1
        else:
            mx+=1
    else:
        g = math.gcd(a,b)
        a //= g
        b //= g
        if (a,b) not in dic:
            dic[(a,b)] =1
        else:
            dic[(a,b)] +=1

ma = max(py,my,px,mx)
for i in dic:
    ma = max(ma,dic[i])

print(ma)