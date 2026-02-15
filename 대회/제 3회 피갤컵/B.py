N, K = map(int, input().split())
S = input()

flag = 0
run = 0
for x in S:
    if x == '0':
        run += 1
        if run >= K:
            print(0)
            flag = 1
            break
    else:
        run = 0
if flag==0:
    print(1)
