import sys
input = sys.stdin.readline

a = input().rstrip()
po = list(input().rstrip())
l = len(po)
now = 0

ans = []
b = ""

for i in a:
    ans.append(i)

    if ans[len(ans)-l:len(ans)] == po:
        for j in range(l):
            ans.pop()

if len(ans)==0:
    print("FRULA")
else:
    for i in ans:
        print(i,end="")