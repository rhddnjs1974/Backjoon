a = int(input())
arr = []
for i in range(a):
    x,y = map(int,input().split())
    arr.append((x,y))
    
arr.sort()
time = 0
for i in arr:
    time = max(time,i[0])+i[1]
print(time)