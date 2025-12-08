import sys
input = sys.stdin.readline

def f(n,T):
    global flag
    if n==len(s):
        if T==s:
            flag = 1
        return 0
    if T[-1]=="A":
        f(n-1,T[:-1])
    if T[0]=="B":
        x = T[1:]
        f(n-1,x[::-1])


s = input().rstrip()
t = input().rstrip()
flag = 0
f(len(t),t)
print(flag)