N = int(input())
arr=  list(map(int,input().split()))

stack = []
now = 1

for i in arr:
    if i==now:
        now+=1
    else:
        stack.append(i)
    while(stack and stack[-1]==now):
        now+=1
        stack.pop()

if stack:
    print("Sad")
else:
    print("Nice")