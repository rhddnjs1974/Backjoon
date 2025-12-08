import sys
input = sys.stdin.readline
########################################


def factorial(a):

    n = 1
    for i in range(1,a+1):
        n*=i
    return n

n,k = map(int,input().split())

A = factorial(n) #분자
B = factorial(k)*factorial(n-k) #분모

print(A//B)