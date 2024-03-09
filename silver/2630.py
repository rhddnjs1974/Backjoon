n = int(input())
arr = []
white = 0
blue = 0

def div(array,N,a,b):
    global white,blue
    wh = 0
    bl = 0
    for i in range(N):
        for j in range(N):
            if array[i+a][j+b]==1:
                bl+=1
            else:
                wh+=1

    if wh==N*N:
        white+=1
    elif bl==N*N:
        blue+=1
    else:
        div(array,N//2,a,b)
        div(array, N // 2, a+N // 2, b)
        div(array, N // 2, a, b+N // 2)
        div(array, N // 2, a+N // 2, b+N // 2)


for i in range(n):
    arr.append(list(map(int,input().split())))

div(arr,n,0,0)

print(white)
print(blue)