import sys
import math
input = sys.stdin.readline

N = int(input())

small = 10000000000000000
big = -10000000000000000
for i in range(N):
    A,B,C = map(int,input().split())
    if A>0:
        small = min(small,(C-B)//A)
    else:
        big = max(big,-((C-B)//-A))
        
if small==10000000000000000 or big==-10000000000000000:
    print(-1)
else:
    if small>=big:
        print(small-big+1)
    else:
        print(0)