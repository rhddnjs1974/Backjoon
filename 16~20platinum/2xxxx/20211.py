import sys
input = sys.stdin.readline

n = int(input())
play = input().rstrip()
exp = 0

numTodd = [0]*((n//2)+2)
numTeven = [0]*((n//2)+2)
numT = [0]*(n+1)


for x in range(n):
    y = x//2
    i = play[x]
    if i=="T":
        
        if exp%2==0:
            exp+=5
        else:
            exp+=1
        
        numT[x] = numT[x-1]+1 
        if x%2==1:
            numTodd[y]=numTodd[y-1]+1
        else:
            numTeven[y]=numTeven[y-1]+1
    else:
        exp += 3
        
        numT[x] = numT[x-1]
        if x%2==1:
            numTodd[y]=numTodd[y-1]
        else:
            numTeven[y]=numTeven[y-1]
        



def calculate(now,next):
    nowp2 = now//2
    nextp2 = next//2
    nowexp = 0
    
    if now%2==0:
        if next%2==0:
            nowexp += (numTeven[nextp2]-numTeven[nowp2])
            nowexp += 5*(numTodd[nextp2-1]-numTodd[nowp2-1])
        else:
            nowexp += (numTeven[nextp2]-numTeven[nowp2])
            nowexp += 5*(numTodd[nextp2]-numTodd[nowp2-1]) 
        
    else:
        if next%2==0:
            nowexp += 5*(numTeven[nextp2]-numTeven[nowp2])
            nowexp += (numTodd[nextp2-1]-numTodd[nowp2])
        else:
            nowexp += 5*(numTeven[nextp2]-numTeven[nowp2])
            nowexp += (numTodd[nextp2]-numTodd[nowp2])
    
    nowexp += 3*(next-now-numT[next]+numT[now])
    
    return nowexp


ans = []
for x in range(1,exp+1):
    now = -1
    level = 0
    
    while(now<n-1):
        left = now+1
        right = n-1
        
        
        while(left<=right):
            mid = (left+right)//2
            
            nowexp = calculate(now,mid)
            
            if nowexp>=x:
                right = mid-1
            else:
                left = mid+1
        
        
        flag= 0
        if left >= n-1:
            nowexp = calculate(now,n-1)
            
            if nowexp<x:
                flag = 1
        
        now = left
        level += 1
    
    if flag==0:
        ans.append((x,level))


print(len(ans))
for i in ans:
    print(*i)