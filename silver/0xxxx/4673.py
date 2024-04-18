import sys
input = sys.stdin.readline
########################################


arr = [0]*10001
ans = []
for a in range(1,10000):
    if arr[a]==0:
        ans.append(a)
        i = a
        while(i<10001 and arr[i]==0):
            arr[i] = 1
            j = i
            k = str(i)
            for x in k:
                j += int(x)

            i = j

for i in ans:
    print(i)
