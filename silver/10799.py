import sys
input = sys.stdin.readline


a = input()
x = []

ans = 0
for j in a:
    if j=="(":
        x.append(1)
        flag = 1
    if j==")":
        x.pop()
        if flag==1:
            ans+=len(x)
        else:
            ans+=1
        flag=0

print(ans)