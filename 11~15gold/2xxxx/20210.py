
from functools import cmp_to_key
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    x = input().rstrip()
    now = []
    t = ""
    for i in x:
        if i.isdigit():
            t+=i
        else:
            if t!="":
                now.append(t)
                t=""
            now.append(i)
    if t!="":
        now.append(t)

    arr.append(now)

def cmp(a,b):
    x = len(a)
    y = len(b)
    for i in range(min(x,y)):
        if cmp2(a[i],b[i])!=0:
            return cmp2(a[i],b[i])
    
    if x>y:
        return 1
    else:
        return -1

def cmp2(a,b):
    if a.isdigit():
        if b.isdigit():
            x = int(a)
            y = int(b)
            if x<y:
                return -1
            elif x==y:
                if len(a)>len(b):
                    return 1
                elif len(a)==len(b):
                    return 0
                else:
                    return -1
            else:
                return 1
        else:
            return -1
    else:
        if b.isdigit():
            return 1
        else:
            return cmp3(a,b)


def cmp3(a,b):
    x=a.upper()
    y=b.upper()
    
    if x>y:
        return 1
    elif x==y:
        if a>b:
            return 1
        elif a==b:
            return 0
        else:
            return -1
    else:
        return -1
    

arr.sort(key=cmp_to_key(cmp))

for i in arr:
    print(*i,sep="")