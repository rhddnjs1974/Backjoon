n = int(input())
ans = 0
for i in range(n):
    a = input()
    flag = 1
    now = 0
    dic={}
    for j in a:
        if j!= now:
            if j not in dic:
                dic[j] = 1
                now = j
            else:
                flag=0
                break
        else:
            continue
    ans+=flag
print(ans)