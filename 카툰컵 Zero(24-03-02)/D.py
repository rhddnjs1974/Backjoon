import sys
input = sys.stdin.readline
from itertools import combinations, permutations
###################################################

A,B = map(int,input().split())
C,D = map(int,input().split())
K = int(input())

toka = A
doldol = A+C

doldol_time = (doldol/D)
if int(doldol_time)<doldol_time:
    doldol_time=int(doldol_time)+1
else:
    doldol_time=int(doldol_time)

if ((K+2*B)**2-8*A*K)<0:
    print(-1)
else:
    if K!=0:
        time = (2*B+K-((K+2*B)**2-8*A*K)**0.5)/(2*K)
    else:
        time = A/B

    if int(time)<time:
        ans = int(time)+1
    else:
        ans = int(time)

    if ans<doldol_time:
        print(ans)
    else:
        print(-1)
