n = int(input())
arr= list(map(int,input().split()))

a = 0
for i in arr:
    a^=i

if a==0:
    print("cubelover")
else:
    print("koosaga")