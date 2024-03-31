import sys
input = sys.stdin.readline
T = int(input())

for i in range(T):
    a,b = map(int,input().split())
    if a*3<=b<=a*4:
        print(0)
    elif b<a*3:
        print(a*3-b)
    else:
        if a==0 and b==1:
            print(3)
        elif a==0 and b==2:
            print(2)
        elif a==1 and b==5:
            print(2)
        elif a==0 and b==5:
            print(3)
        else:
            b -= a*4
            print(1+(b-1)//4)