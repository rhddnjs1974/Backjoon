import sys
input = sys.stdin.readline


for _ in range(int(input())):
    x,y,z = map(int,input().split())
    flag = 0
    for k in range(31):
        if ((x>>k)&1) + ((y>>k)&1) + ((z>>k)&1) == 2:
            flag = 1
    if flag==1:
        print("NO")
    else:
        print("YES")