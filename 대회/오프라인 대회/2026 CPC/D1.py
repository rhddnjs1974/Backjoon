import sys
input = sys.stdin.readline

N, K = map(int,input().split())

t = K+1

left = [1]
right = [N]

lnum = 2
rnum = t
while(lnum<rnum):
    if left[-1]<right[-1]:
        right.append(lnum)
        left.append(rnum)
    else:
        right.append(rnum)
        left.append(lnum)
        
    lnum += 1
    rnum -= 1

if lnum==rnum:
    left.append(lnum)

for x in range(len(right)-1,-1,-1):
    left.append(right[x])

ans = 0
for i in range(len(left)-1):
    ans += left[i]*left[i+1]
print(ans)