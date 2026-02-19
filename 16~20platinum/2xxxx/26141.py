dx, dy = map(int, input().split())
grid = [input().rstrip() for _ in range(dy)]

markers = []
for j in range(dy):
    y = dy - j
    row = grid[j]
    for i in range(dx):
        if row[i] == 'X':
            markers.append((i + 1, y))

R = max(dx, dy) - 1
side = 2 * R + 1
T = side * side
bits_len = T
byte_len = (T + 7) // 8

time_map = [[-1] * side for _ in range(side)]

x = 0
y = 0
t = 0
time_map[y + R][x + R] = 0

step = 1
while t + 1 < T:
    for _ in range(step):
        if t + 1 >= T:
            break
        y += 1
        t += 1
        if -R <= x <= R and -R <= y <= R:
            time_map[y + R][x + R] = t
    for _ in range(step):
        if t + 1 >= T:
            break
        x += 1
        t += 1
        if -R <= x <= R and -R <= y <= R:
            time_map[y + R][x + R] = t
    step += 1
    for _ in range(step):
        if t + 1 >= T:
            break
        y -= 1
        t += 1
        if -R <= x <= R and -R <= y <= R:
            time_map[y + R][x + R] = t
    for _ in range(step):
        if t + 1 >= T:
            break
        x -= 1
        t += 1
        if -R <= x <= R and -R <= y <= R:
            time_map[y + R][x + R] = t
    step += 1

def set_bit(buf, pos):
    bi = pos >> 3
    bj = 7 - (pos & 7)
    buf[bi] |= (1 << bj)

seqs = []
idx_to_xy = []

idx = 0
for yy in range(1, dy + 1):
    for xx in range(1, dx + 1):
        buf = bytearray(byte_len)
        for mx, my in markers:
            dx0 = mx - xx
            dy0 = my - yy
            if -R <= dx0 <= R and -R <= dy0 <= R:
                tt = time_map[dy0 + R][dx0 + R]
                if tt >= 0:
                    set_bit(buf, tt)
        b = bytes(buf)
        seqs.append((b, idx))
        idx_to_xy.append((xx, yy))
        idx += 1

seqs.sort(key=lambda x: x[0])

def lcp_bits(a, b):
    n = len(a)
    i = 0
    while i < n and a[i] == b[i]:
        i += 1
    if i == n:
        return bits_len
    diff = a[i] ^ b[i]
    lead0 = 8 - diff.bit_length()
    v = i * 8 + lead0
    if v > bits_len:
        v = bits_len
    return v

need = [0] * (dx * dy)

for i in range(len(seqs)):
    b, idx0 = seqs[i]
    best = 0
    if i > 0:
        best = lcp_bits(b, seqs[i - 1][0])
    if i + 1 < len(seqs):
        v = lcp_bits(b, seqs[i + 1][0])
        if v > best:
            best = v
    need[idx0] = best

total = 0.0
mx_need = 0
for v in need:
    total += v
    if v > mx_need:
        mx_need = v

coords = []
for i, v in enumerate(need):
    if v == mx_need:
        coords.append(idx_to_xy[i])

coords.sort(key=lambda p: (p[1], p[0]))

print(total / (dx * dy))
print(mx_need)
for x, y in coords:
    print("("+str(x)+","+str(y)+")",end=" ")
