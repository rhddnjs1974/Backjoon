arr = []

for i in range(5):
    arr.append(input())

for j in range(15):
    for i in range(5):

        try:
            print(arr[i][j],end="")
        except:
            continue