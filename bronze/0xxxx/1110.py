n = int(input())

ans = 1
m = n
if m < 10:
    m *= 11
else:
    x = (m % 10 + m // 10) % 10
    m = 10 * (m % 10) + x


while(True):
    if m==n:
        break
    if m < 10:
        m *= 11
    else:
        x = (m % 10 + m // 10) % 10
        m = 10 * (m % 10) + x
    ans+=1

print(ans)