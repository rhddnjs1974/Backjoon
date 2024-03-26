import sys
input = sys.stdin.readline

S = input().rstrip()
t = S[0]
x = 0
for i in S:
    if i!=t:
        t=i
        x+=1

print((x+1)//2)