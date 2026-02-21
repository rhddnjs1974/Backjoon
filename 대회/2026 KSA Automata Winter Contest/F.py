import sys
import random

input = sys.stdin.readline

n=int(input())
find = (n//2)+1
dp = [0]*(n+1) #0:모름 1:아님
while(True):

    arr = list(range(1,n+1))
    random.shuffle(arr)
    print("?",*arr,flush=True)
    l,r,h = map(int,input().split())
    if h==find:
        x=set()
        for i in range(l-1,r):
            x.add(arr[i])
        for i in range(1,n+1):
            if i not in x:
                dp[i]=1
    elif h>find:
        for i in range(l-1,r):
            dp[arr[i]]=1

    if sum(dp)==n-1:
        for i in range(1,n+1):
            if dp[i]==0:
                print("!",i,flush=True)
                break
        break