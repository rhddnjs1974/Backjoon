n = int(input())
arr= list(map(int,input().split()))

a = 0
f = 0
for i in arr:
    a^=i
    if i>1:
        f = 1
        
if (a==0 and f==1) or (a==1 and f==0):
    print("cubelover")
else:
    print("koosaga")