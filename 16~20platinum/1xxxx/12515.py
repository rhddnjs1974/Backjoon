T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    m=0
    for i, x in enumerate(arr, start=1):
        if x!=i:
            m+=1

    print("Case #%d: %.6f"%(t,m))

