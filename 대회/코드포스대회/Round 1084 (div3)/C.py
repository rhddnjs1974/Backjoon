import sys
input = sys.stdin.readline

for testcase in range(int(input())):
    n = int(input())
    s = input().rstrip()

    arr = []
    for x in s:
        if arr and arr[-1] == x:
            arr.pop()
        else:
            arr.append(x)

    if arr:
        print("NO")
    else:
        print("YES")