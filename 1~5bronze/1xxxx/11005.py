N, B = map(int, input().split())
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = ""
while N:
    ans += str(arr[N%B])
    N //= B

t = ans[::-1]
print(t)