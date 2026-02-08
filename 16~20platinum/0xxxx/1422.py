import sys
input = sys.stdin.readline

K, N = map(int, input().split())

arr = []
mx = ""
i = 0
while i < K:
    s = input().strip()
    arr.append(s)

    if mx == "":
        mx = s
    else:
        if len(s) > len(mx):
            mx = s
        elif len(s) == len(mx):
            if s > mx:
                mx = s
    i += 1

extra = N - K
i = 0
while i < extra:
    arr.append(mx)
    i += 1

arr.sort(key=lambda x: x * 10,reverse=True)

for s in arr:
    print(s, end="")
