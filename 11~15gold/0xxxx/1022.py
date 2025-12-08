import sys
input = sys.stdin.readline

r1,c1,r2,c2 = map(int,input().split())

array = [[0] * (c2-c1+1) for i in range(r2-r1+1)]


x,y = 0,0
a=1
dx = [0,-1,0,1]
dy = [1,0,-1,0]
s = 0
l=0
dir=0
while(True):
    l+=1
    for i in range(2):
        for j in range(l):
            if r1<=x<=r2 and c1<=y<=c2:
                array[x-r1][y-c1] = a
                s+=1
            x+= dx[dir]
            y+= dy[dir]
            a+=1
        
        dir = (dir+1) % 4
    
    
    if s==(c2-c1+1)*(r2-r1+1):
        break


max_l = 0
for i in array:
    for j in i:
        max_l = max(max_l,len(str(j)))
        
for i in array:
    for j in i:
        print(str(j).rjust(max_l),end=" ")
    print()