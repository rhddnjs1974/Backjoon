a,b = map(int,input().split())

for i in range(1001):
    print(a//b,end="")
    if i==0:
        print(".",end="")
    a = (a%b) * 10