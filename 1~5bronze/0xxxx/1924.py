x,y = map(int,input().split())

t=0

month=[31,28,31,30,31,30,31,31,30,31,30,31]

for i in range(x-1):
    t+=month[i]
t+=y
t%=7

arr=["SUN","MON","TUE","WED","THU","FRI","SAT"]
print(arr[t])