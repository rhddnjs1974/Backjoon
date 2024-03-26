def div(array,N,a,b):

    wh = 0 # 0
    bl = 0 # 1

    for i in range(N):
        for j in range(N):
            if array[i+a][j+b]==1:
                bl+=1
            else:
                wh+=1

    if wh==N*N:
        print(0,end="")
    elif bl==N*N:
        print(1,end="")
    else:
        print("(", end="")
        div(array,N//2,a,b)
        div(array, N // 2, a, b + N // 2)
        div(array, N // 2, a+N // 2, b)
        div(array, N // 2, a+N // 2, b+N // 2)
        print(")",end="")

n = int(input())
arr = []
white = 0
blue = 0


for i in range(n):
    ar = input()
    arr.append([])
    for j in ar:
        arr[i].append(int(j))

div(arr,n,0,0)

