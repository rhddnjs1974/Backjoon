import sys
input = sys.stdin.readline

n = int(input())
arr= list(input().split())

num0 = arr.count("0")
if num0==n:
    print(0)
else:
    for i in range(n-1,0,-1):
        for j in range(i):
            a = arr[j]
            b = arr[j+1]
            ab = a+b
            ba = b+a
            if int(ab)<int(ba):
                arr[j],arr[j+1] = arr[j+1],arr[j]

    ans = ""
    for i in arr:
        ans+=i
    print(ans)