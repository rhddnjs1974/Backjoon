import sys
input = sys.stdin.readline

n, k = map(int,input().split())
arr = [0]+list(map(int,input().split()))

start = 1

tr = 0
robot = [0]*(2*n+1)

kk = 0

while(tr<50 and kk<k):

    tr+=1

    start -= 1
    if start==0:
        start = 2*n

    end = start+n-1
    end %= 2*n
    if end==0:
        end = 2*n

    robot[end] = 0

    if robot[start]==0 and arr[start]>0:
        arr[start]-=1
        robot[start] = 1
        if arr[start]==0:
            kk+=1

    for i in range(2*n,1,-1):
        robot[i] = robot[i-1]
    robot[1] = robot[2*n]

    robot[end] = 0
    print(robot)

    for i in range(2*n+end-1,2*n+start-1,-1):
        i%=2*n
        if i==0:
            i = 2*n

        if robot[i]==0:
            continue

        if robot[i+1]==0 and arr[i+1]>0:
            robot[i] = 0

            arr[i+1] -= 1
            if arr[i+1]==0:
                kk+=1
            if i!=end-1:
                robot[i+1] = 1

    print(arr)
    print(robot)
    print(start)

print(tr)