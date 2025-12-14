import re

for i in range(int(input())):
    sign = input()
    p = re.compile('(100+1+|01)+')

    if p.fullmatch(sign):
        print("YES")
    else:
        print("NO")