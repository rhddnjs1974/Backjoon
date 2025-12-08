import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline
def post(s, e):
    if s > e:
        return
    mid = e + 1

    for i in range(s + 1, e + 1):
        if arr[s] < arr[i]:
            mid = i
            break

    post(s + 1, mid - 1)
    post(mid, e)
    print(arr[s])

arr = []

while True:
    try:
        arr.append(int(input()))
    except:
        break



post(0, len(arr) - 1)