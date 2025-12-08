n = int(input())
la = 1
ra = n
lb = 1
rb = n

while(la<ra and lb<rb):
    mida = (la+ra)//2
    midb = (lb+rb)//2
    
    print("? A",mida,flush=True)
    aa = int(input())
    print("? B",midb,flush=True)
    bb = int(input())
    
    if aa>bb:
        ra = mida
        lb = midb+1
    else:
        rb = midb
        la = mida+1

mida = (la+ra)//2
midb = (lb+rb)//2
print("? A",mida,flush=True)
aa = int(input())
print("? B",midb,flush=True)
bb = int(input())
print("!",min(aa,bb),flush=True)