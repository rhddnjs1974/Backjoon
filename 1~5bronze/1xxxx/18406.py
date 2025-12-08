N = input()
t = len(N)//2
left = 0
right = 0
for i in range(t):
    left+=int(N[i])
    right+=int(N[t+i])

if left==right:
    print("LUCKY")
else:
    print("READY")