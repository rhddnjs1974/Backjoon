import sys
input = sys.stdin.readline

mi = 0
ma = 11
while(True):
    a = int(input())
    if a==0:
        break
    b = input().rstrip()
    
    if b=="too high":
        ma = min(ma,a)
    elif b=="too low":
        mi = max(mi,a)
    else:
        if mi<a<ma:
            print("Stan may be honest")
        else:
            print("Stan is dishonest")
        mi = 0
        ma = 11