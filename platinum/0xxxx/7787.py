import sys
input = sys.stdin.readline

r,g = map(int,input().split())

for i in range(1,50):
    if r % (2**i) == 2**(i-1):
        gr = i
        break

for i in range(1,50):
    if g % (2**i) == 2**(i-1):
        gg = i
        break

a = gr^gg
if a==0:
    print("B player wins")
else:
    print("A player wins")