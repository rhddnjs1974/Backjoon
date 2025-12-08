import sys
import math
input = sys.stdin.readline

s, p = map(int, input().split())
logp = math.log(p)

# before binary search
value_1 = (s // math.e) * math.log(s / (s // math.e)) if s // math.e else -10 ** 8 # s < math.e 케이스 대응
value_2 = (s // math.e + 1) * math.log(s / (s // math.e + 1))

if logp > max(value_1, value_2): # 존재 불가능
    print(-1)
    exit()

argmax_num = s // math.e if value_1 >= value_2 else s // math.e + 1

# binary search
lower = 1
upper = argmax_num
answer = []

while lower <= upper:
    mid = (lower + upper) // 2
    temp = mid * math.log(s / mid)
    if temp < logp:
        lower = mid + 1
    elif temp >= logp:
        answer.append(mid)
        upper = mid - 1

min_number = int(min(answer))
print(2 if min_number == 1 and s != p else min_number)