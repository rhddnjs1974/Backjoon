import sys
input = sys.stdin.readline
from itertools import combinations, permutations
###################################################

x = input().rstrip()
if len(x)<=2:
    print("CE")
elif x[0]=="\"" and x[-1]=="\"":
    if x[1]==" " and x[-2]==" ":
        print("CE")
    else:
        print(x[1:-1])
else:
    print("CE")