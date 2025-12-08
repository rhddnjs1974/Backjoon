import sys
import random
input = sys.stdin.readline


x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
x = list(x)



for case in range(int(input())):
    n = int(input())
    arr= list(input().rstrip().split())
    
    for iii in range(10000):
        random.shuffle(x)
        y = ""
        for i in x:
            y+=i
            
        flag = 0
        for a in arr:
            if a in y:
                flag=1
                break
        
        if flag==0:
            ans=y
            break
        
    if iii==9999:
        print("Case #%d: IMPOSSIBLE"%(case+1))
    else:
        print("Case #%d: %s"%(case+1,ans))

            