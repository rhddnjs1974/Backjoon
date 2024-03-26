arr = []
for i in range(9):
    arr.append(int(input()))

ma = max(arr)
print(ma)
print(arr.index(ma)+1)