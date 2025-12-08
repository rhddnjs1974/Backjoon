arr = []
for i in range(9):
    arr.append(list(map(int,input().split())))

ma = -1
for i in range(9):
    for j in range(9):
        if ma<arr[i][j]:
            x = i
            y = j
            ma = arr[i][j]

print(ma)
print(x+1,y+1)