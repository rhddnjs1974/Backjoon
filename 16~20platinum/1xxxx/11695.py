n,m = map(int,input().split())
arr = []
for i in range(n):
    a= list(map(int,input().split()))
    arr.append(sum(a))
    
a = 0
for i in arr:
    a^=i

if a==0:
    print("ainta")
else:
    print("august14")