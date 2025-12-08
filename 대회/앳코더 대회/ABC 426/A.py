import sys
input = sys.stdin.readline

x,y = input().split()

if x=="Ocelot":
    x=1
elif x=="Serval":
    x=2
else:
    x=3

if y=="Ocelot":
    y=1
elif y=="Serval":
    y=2
else:
    y=3
    
if x>=y:
    print('Yes')
else:
    print('No')