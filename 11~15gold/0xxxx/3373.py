import sys
input = sys.stdin.readline

N = int(input())
card = [tuple(map(int, input().split())) for _ in range(N)]

ba = 0
arr = []

for a, b in card:
    ba -= max(a,b)
    arr.append(a + b)  

arr.sort()

print(ba + sum(arr[:N//2]))
