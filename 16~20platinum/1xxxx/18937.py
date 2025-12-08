import sys
input = sys.stdin.readline

n = int(input())
arr= list(map(int,input().split()))

a = 0
for i in arr:
    a^=(i-2)


who = input().rstrip()

if a==0:
    if who=="Whiteking":
        print("Blackking")
    else:
        print("Whiteking")
else:
    print(who)