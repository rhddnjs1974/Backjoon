a = '9780921418'
for i in range(3):
    a += input()

t=0
ans = 0
for i in a:
    t+=1
    if t%2==1:
        ans+= int(i)
    else:
        ans+= int(i)*3

print("The 1-3-sum is",ans)