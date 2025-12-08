f=0
for a in range(1, 10000):
    print("? A", a, flush=True)
    resp = int(input())

    if resp == 1:
        f=1
        break
if f==0:
    a=10000
f=0
for b in range(1, 10000):
    if b==3000:
        continue
    
    print("? B", b, flush=True)
    resp = int(input())

    if resp == 1:
        f=1
        break

if f==0:
    b=10000   
print("!", a + b)
