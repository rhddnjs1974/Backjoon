import sys
input = sys.stdin.readline
from itertools import combinations, permutations
###################################################

point = int(input())

if 90<=point<=100:
    print("A")
elif 80<=point:
    print("B")
elif 70<=point:
    print("C")
elif 60<=point:
    print("D")
else:
    print("F")