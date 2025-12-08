import sys
input = sys.stdin.readline

S = input().rstrip()
for i in range(len(S)):
    if i==len(S)//2:
        continue
    print(S[i],end="")