import sys
input = sys.stdin.readline

while True:
    s = input().strip()
    if s == '0':
        break
    if s == s[::-1]:
        print("yes")
    else:
        print("no")
