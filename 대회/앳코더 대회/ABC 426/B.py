import sys
input = sys.stdin.readline

s = input().rstrip()
dic = {}

for i in s:
    if i in dic:
        dic[i] +=1
    else:
        dic[i] = 1

for i in dic:
    if dic[i]==1:
        print(i)