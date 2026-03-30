import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())

arr = [[-1]*M for i in range(N)]


dc = [-1,1,0,0]
dr = [0,0,-1,1]
def hurtwithme(x,y,d):
    


for i in range(K):
    r,c,l, D = input().split()
    D = D.rstrip()
    r = int(r)
    c = int(c)
    l = int(l)

    arr[r][c] = (i,0)
    for j in range(l):
        if D[j]=="L":
            c-=1
        if D[j]=="R":
            c+=1
        if D[j]=="U":
            r-=1
        if D[j]=="D":
            r+=1
        arr[r][c] = (i,j+1)
    
    if hurtwithme(r,c,D[-1]):