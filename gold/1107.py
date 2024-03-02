import sys
input = sys.stdin.readline
from itertools import combinations, permutations
###################################################

n = int(input())
broke = int(input())
broke_list=[]
if broke!=0:
    broke_list = list(map(int,input().split()))

ans = 0

while(True):
    x = n - ans
    if x<0:
        x=0
    y = n + ans
    x = str(x)
    y = str(y)
    flag = 0
    for i in broke_list:
        if str(i) in x:
            flag=1
            break
    if flag==0:
        print(min(ans + len(x),abs(100-n)))
        break
    flag = 0
    for i in broke_list:
        if str(i) in y:
            flag = 1
            break
    if flag == 0:
        print(min(ans + len(y),abs(100-n)))
        break
    ans+=1
    if ans>500001:
        print(abs(100-n))
        break

