import sys
input = sys.stdin.readline

S = input()
a = set()
for i in range(len(S)):
    for j in range(i+1,len(S)):
        t = S[i:j]
        a.add(t)

print(len(a))