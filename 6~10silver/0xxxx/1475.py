import math
n = input()
arr = [0]*10
for i in n:
    x = int(i)
    if x==6 or x==9:
        arr[6]+=0.5
    else:
        arr[x]+=1

print(int(math.ceil(max(arr))))