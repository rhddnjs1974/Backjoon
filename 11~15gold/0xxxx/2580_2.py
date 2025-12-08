
def sudoku(n):
    global flag,count0
    if flag==1:
        return
    if n==count0:
        for i in arr:
            print(*i)
        flag=1
        return
    x,y = blank[n]
    tx = (x//3)*3
    ty = (y//3)*3
    for number in range(1,10):
        notuse = 0
        for i in range(9):
            if arr[(x+i)%9][y]==number:
                notuse=1
                break
            if arr[x][(y+i)%9]==number:
                notuse=1
                break
        for i in range(3):
            for j in range(3):
                if arr[tx+i][ty+j]==number:
                    notuse=1
                    break
        if notuse==0:
            arr[x][y] = number
            sudoku(n+1)
            arr[x][y] = 0

arr = []

for i in range(9):
    x = input()
    arr.append([])
    for a in x:
        arr[-1].append(int(a))

    
count0 = 0
blank = []

for i in range(9):
    for j in range(9):
        if arr[i][j]==0:
            count0 +=1

            blank.append((i,j))

flag =0
            
sudoku(0)
