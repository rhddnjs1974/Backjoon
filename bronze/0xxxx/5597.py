arr = [0]*31

for i in range(28):
    n = int(input())
    arr[n]= 1

for i in range(1,31):
    if arr[i]==0:
        print(i)