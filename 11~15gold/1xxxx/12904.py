a = list(input())
b = list(input())

ans=0
while(b):
    if b[-1]=="A":
        b.pop()
    else:
        b.pop()
        b.reverse()
    
    if a==b:
        ans=1
        break
print(ans)