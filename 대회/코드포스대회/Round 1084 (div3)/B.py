import sys
input = sys.stdin.readline

for testcase in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    flag = 1
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            flag = 0
            break
        
    if flag==0:
        print(1)
    else:
        print(n)
