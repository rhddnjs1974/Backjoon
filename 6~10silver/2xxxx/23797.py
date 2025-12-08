import sys
input = sys.stdin.readline
import copy

S = input().rstrip()
N = len(S)

if S[0]=="P":
    p = 1
    k = 0
else:
    k = 1
    p = 0

ans = 0
for i in S[1:]:
    if i =="P":
        p+=1
        k = max(0,k-1)
    else:
        k+=1
        p = max(0,p-1)
    
    ans = max(p,k,ans)
print(max(ans,1))