import sys
input = sys.stdin.readline

r,s = map(int,input().split())
arr = []
mishop = [10000]*s
maX = [-10000]*s
stack = []
for i in range(r):
    t = input().rstrip()
    arr.append([])
    for x in range(len(t)):
        if t[x]=="#":
            mishop[x]=min(mishop[x],i)
            arr[-1].append("#")
        elif t[x]=="X":
            stack.append((i,x))
            maX[x] = max(maX[x],i)
            arr[-1].append(".")
        else:
            arr[-1].append(".")

drop = 10000
for i in range(s):
    drop = min(drop,mishop[i]-maX[i]-1)

for a,b in stack:
    arr[a+drop][b] = "X"

for a in arr:
    for j in a:
        print(j,end="")
    print()