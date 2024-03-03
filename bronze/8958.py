T = int(input())
for i in range(T):
    x = input()
    ans = 0
    now = 0
    for i in x:
        if i=="O":
            now+=1
            ans+=now
        else:
            now=0
    print(ans)