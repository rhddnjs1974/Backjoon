import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

stack = []
ans = 0

for i in range(N):
    t = arr[i]
    time = 0
    time2 = 1
    while(stack):
        if stack[-1][0]<t:
            a,b = stack.pop()
            time+=b
        elif stack[-1][0]==t:
            a,b = stack.pop()
            time2+=b
        else:
            break

    if stack:
        ans+=1

    ans+=(time+time2-1)

    stack.append((t,time2))


print(ans)