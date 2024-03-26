import sys
input = sys.stdin.readline

while(True):
    a = input().rstrip()
    if a==".":
        break
    x = []
    flag= 0
    for j in a:
        if j=="(":
            x.append(1)
        if j=="[":
            x.append(2)
        if j==")":
            if x:
                t = x.pop()
                if t!=1:
                    flag=1
                    break
            else:
                flag=1
                break
        if j=="]":
            if x:
                t = x.pop()
                if t!=2:
                    flag=1
                    break
            else:
                flag=1
                break
    if flag==1 or len(x)>0:
        print("no")
    else:
        print("yes")