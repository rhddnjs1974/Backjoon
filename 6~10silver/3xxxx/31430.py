
def code(a):
    x = ""
    for i in range(12,-1,-1):
        b = a//(26**i)
        a = a%(26**i)
        x+=chr(97+b)
    return x

def decode(a):
    ans = 0
    m = 12
    for i in a:
        ans+= (ord(i)-97)*(26**m)
        m-=1
    return ans

t = int(input())
if t==1:
    a,b = map(int,input().split())
    print(code(a+b))
else:
    a = input()
    print(decode(a))