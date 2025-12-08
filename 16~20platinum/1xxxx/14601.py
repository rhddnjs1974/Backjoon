import sys
sys.setrecursionlimit(100000)
def check(a,b,l):
    for i in range(a,a+l):
        for j in range(b,b+l):
            if arr[i][j]!=0:
                return False
    return True

def rec(a,b,l):
    global n
    n+=1
    if (check(a,b,l//2)):
        arr[a+l//2-1][b+l//2-1]=n
    if (check(a,b+l//2,l//2)):
        arr[a+l//2-1][b+l//2]=n
    if (check(a+l//2,b,l//2)):
        arr[a+l//2][b+l//2-1]=n
    if (check(a+l//2,b+l//2,l//2)):
        arr[a+l//2][b+l//2] = n
    if l==2:
        return
    
    rec(a,b,l//2)
    rec(a,b+l//2,l//2)
    rec(a+l//2,b,l//2)
    rec(a+l//2,b+l//2,l//2)
    
k = int(input())
x,y = map(int,input().split())

n = 0
l = 2**k
arr = [[0]*l for i in range(l)]
arr[x-1][y-1] = -1

rec(0,0,l)

for i in range(l-1,-1,-1):
    for j in range(l):
        print(arr[j][i],end=" ")
    print()