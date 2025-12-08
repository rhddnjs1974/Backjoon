ja,mo = map(int,input().split())
x, a = map(int,input().split())
x0 = int(input())
print(x*x0+a)
if x==0:
    print('0 0')
else:
    print(ja, mo*abs(x))