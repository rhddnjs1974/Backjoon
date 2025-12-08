

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if S[arr[j]]*T[arr[j+1]] < S[arr[j+1]]*T[arr[j]]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

n = int(input())
T =[0]
S =[0]
arr=[]
for i in range(n):
    arr.append(i+1)
    x,y = map(int,input().split())
    T.append(x)
    S.append(y)
bubbleSort(arr)
print(*arr)