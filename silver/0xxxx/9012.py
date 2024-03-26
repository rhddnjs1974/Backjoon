import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    a = input()
    x = []
    flag= 0
    for j in a:
        if j=="(":
            x.append(1)
        if j==")":
            if x:
                x.pop()
            else:
                flag=1
                break

    if flag==1 or len(x)>0:
        print("NO")
    else:
        print("YES")