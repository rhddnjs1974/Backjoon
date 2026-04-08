import sys
input = sys.stdin.readline

s = input().strip()
pos = s.index('*')
total = 0
for i in range(13):
    if i == pos:
        continue
    if i%2 == 0:
        total += int(s[i])
    else:
        total += int(s[i]) * 3

if pos%2 == 0:
    w = 1
else:
    w = 3

for d in range(10):
    if (total+d * w) % 10 == 0:
        print(d)
        break
