import sys
input = sys.stdin.readline

n = int(input())
P = input().rstrip()
Q = input().rstrip()
R = input().rstrip()

def first_d(a,b):
    for i in range(n):
        if a[i]!=b[i]:
            return True, (a[i],b[i])
    return False, (0,0)

o1, (x1,y1) = first_d(P,Q)
o2, (x2,y2) = first_d(Q,R)

if o1==False or o2==False:
    print("Hmm...")
    exit()

if x1==y2 and x2==y1:
    print("Hmm...")
else:
    print("HJS! HJS! HJS!")