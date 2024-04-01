import sys
input = sys.stdin.readline
from itertools import combinations, permutations
###################################################

N = int(input())
arr=[]
for i in range(N):
    arr.append(input())

for i in range(N):
    print("? %s"%(arr[i]))
    sys.stdout.flush()
    x = int(input())
    if x==1:
        print("! %s"%(arr[i]))
        sys.stdout.flush()
        break
    print("? %s" % (arr[i]))
    sys.stdout.flush()
    x = int(input())
    if x == 1:
        print("! %s" % (arr[i]))
        sys.stdout.flush()
        break
