import sys
input = sys.stdin.readline

def ccw(x1,y1,x2,y2,x3,y3):
    c = (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
    return c

x=0
T = int(input())
for i in range(T):
    N = int(input())
    arr= []
    for i in range(N):
        arr.append(list(map(int,input().split())))

    ans = 0
    for i in range(1,N-1):
        ans+= ccw(*arr[0],*arr[i],*arr[i+1])
    x += abs(ans)

print(int(x*0.5))