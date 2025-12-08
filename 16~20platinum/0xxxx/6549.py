import sys
input = sys.stdin.readline

while(True):

    N,*arr = map(int,input().split())
    if N==0:
        break
    arr.append(0)
    ans = 0
    stack = []
    for i in range(N+1):
        t = arr[i]
        num = 0
        while(stack):
            if stack[-1][0]<=t:
                break
            a,b,c = stack.pop()
            num+=c
            ans=max(ans,a*(i-b+c-1))

        stack.append((t,i,1+num))


    print(ans)
