import sys
input = sys.stdin.readline

def bt(now,x):
    global n,ansma,ansmi
    if x==n:
        ansma = max(ansma,now)
        ansmi = min(ansmi,now)
    for i in range(4):
        if arr2[i]==0:
            continue
        arr2[i]-=1
        if i==0:
            bt(now+arr[x],x+1)
        if i==1:
            bt(now-arr[x],x+1)
        if i==2:
            bt(now*arr[x],x+1)
        if i==3:
            if now>=0:
                bt(now//arr[x],x+1)
            else:
                bt( -(-now//arr[x]),x+1)
        arr2[i]+=1



n = int(input())
arr = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

ansma = -1e10
ansmi = 1e10

bt(arr[0],1)

print(ansma)
print(ansmi)





