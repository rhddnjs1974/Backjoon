
N = int(input())

time = [4,6,4,10]
dic = {}
for week in range(N):
    for i in range(4):
        a = input().split()
        for x in a:
            if x=="-":
                continue
            if x in dic:
                dic[x] += time[i]
            else:
                dic[x] = time[i]

workma = 0
workmi = 10000000

for i in dic:
    workma = max(workma,dic[i])
    workmi = min(workmi,dic[i])

if workma-workmi<=12:
    print("Yes")
else:
    print("No")
