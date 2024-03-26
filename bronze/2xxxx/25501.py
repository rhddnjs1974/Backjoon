def recursion(s, l, r):
    global x
    x+=1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

T = int(input())
for i in range(T):
    a = input()
    x = 0
    print(isPalindrome(a),x)