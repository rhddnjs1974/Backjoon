
A,B,C = map(int,input().split())
x1,x2,y1,y2 = map(int,input().split())

p = 0
m = 0

if A*x1+B*y1+C>0:
    p+=1
if A*x1+B*y1+C<0:
    m+=1
    
if A*x1+B*y2+C>0:
    p+=1
if A*x1+B*y2+C<0:
    m+=1
    
if A*x2+B*y1+C>0:
    p+=1
if A*x2+B*y1+C<0:
    m+=1
    
if A*x2+B*y2+C>0:
    p+=1
if A*x2+B*y2+C<0:
    m+=1

if p>0 and m>0:
    print("Poor")
else:
    print("Lucky")