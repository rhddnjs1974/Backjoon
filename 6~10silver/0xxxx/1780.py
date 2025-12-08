import sys
input = sys.stdin.readline
########################################
def div(array,N,a,b):
    global x,y,z
    xx = 0
    yy = 0
    zz = 0
    for i in range(N):
        for j in range(N):
            if array[i+a][j+b]==-1:
                xx+=1
            elif array[i+a][j+b]==0:
                yy+=1
            else:
                zz+=1

    if xx==N*N:
        x+=1
    elif yy==N*N:
        y+=1
    elif zz==N*N:
        z+=1
    else:
        if N==3:
            x+=xx
            y+=yy
            z+=zz
        else:
            m = N//3
            div(array,m,a,b)
            div(array, m, a+m, b)
            div(array, m, a+2*m, b)
            div(array, m, a, b+m)
            div(array, m, a+m, b+m)
            div(array, m, a+2*m, b+m)
            div(array, m, a, b+2*m)
            div(array, m, a+m, b+2*m)
            div(array, m, a+2*m, b+2*m)


n = int(input())
arr = []
x = 0 #-1
y = 0 #0
z = 0 #1

for i in range(n):
    arr.append(list(map(int,input().split())))

div(arr,n,0,0)

print(x)
print(y)
print(z)