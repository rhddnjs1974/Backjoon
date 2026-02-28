import sys
input = sys.stdin.readline

def calculate(a):
    n = len(a)
    if n == 0:
        return 0
    
    arr = a + a
    
    i = 0
    j = 1
    k = 0
    
    while i < n and j < n and k < n:
        if arr[i+k] == arr[j+k]:
            k += 1
        elif arr[i+k] < arr[j+k]:
            j += (k+1)
            if i == j:
                j += 1
            k = 0
        else:
            i += (k+1)
            if i == j:
                i += 1
            k = 0
    return min(i, j)
 
 
for testcase in range(int(input())):
    n, x, y = map(int, input().split())
    p = list(map(int, input().split()))

    b = p[x:y]
    
    if x==y:
        print(*p)
        continue
    
    s = calculate(b)
    
    arr1 = b[s:] + b[:s]
    arr2 = p[:x] + p[y:]
    if len(arr2)==0:
        print(*arr1)
        continue

    point = len(arr2)
    for i in range(len(arr2)):
        if arr2[i] > arr1[0]:
            point = i
            break

    ans = arr2[:point] + arr1 + arr2[point:]
    print(*ans)