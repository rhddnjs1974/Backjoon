n = int(input())
print("? 1",flush=True)
a = int(input())
print("?",n,flush=True)
b = int(input())

if a==b:
    print("!",0,flush=True)
elif a<b:
    print("!",1,flush=True)
else:
    print("!",-1,flush=True)