import sys
input = sys.stdin.readline

# 문제 정의 방향(키보드)과 델타
DIRS = [
    ('A', (-1, 0)),
    ('Q', (-1, 1)),
    ('W', ( 0, 1)),
    ('E', ( 1, 1)),
    ('D', ( 1, 0)),
    ('C', ( 1,-1)),
    ('X', ( 0,-1)),
    ('Z', (-1,-1)),
]
# 역맵: (dx,dy) -> key
DELTA_TO_KEY = {d: k for k, d in DIRS}

def sign(v):
    return (v>0) - (v<0)

def cheb(x, y):
    return max(abs(x), abs(y))

n = int(input().strip())
heroes = []
for i in range(n):
    x, y = map(int, input().split())
    heroes.append({
        'x': x, 'y': y,
        'idx': i,
        'instr': [],
        'visited': {(x, y)},
        'done': False,
    })

remaining = n

def occupied_now():
    """현재 시점의 (0,0) 제외 점유 맵"""
    occ = {}
    for h in heroes:
        if not h['done']:
            pos = (h['x'], h['y'])
            if pos != (0, 0):
                occ[pos] = h['idx']
    return occ

def candidates_for(h, entering_now=False):
    """해당 용사의 후보 이동 (문자, 다음좌표) 리스트(우선순위 순)"""
    x, y = h['x'], h['y']

    # 이번 틱에 (0,0)으로 '승인된' 한 명
    if entering_now:
        dx = -sign(x)
        dy = -sign(y)
        key = DELTA_TO_KEY[(dx, dy)]
        return [(key, (x + dx, y + dy))]

    cx, cy = -sign(x), -sign(y)  # 원점 방향
    pref = []

    # 1) d 감소 후보
    if x != 0 and y != 0:
        pref.append((cx, cy))          # 대각
    elif x != 0:
        pref.append((cx, 0))           # x만 줄이기
    elif y != 0:
        pref.append((0, cy))           # y만 줄이기

    # 근접 대체(여전히 d를 줄이는 것들)
    alt_reduce = [(cx, 0), (0, cy), (cx, -cy), (-cx, cy)]
    for dx, dy in alt_reduce:
        if (dx, dy) == (0, 0) or (dx, dy) in pref:
            continue
        if cheb(x + dx, y + dy) < cheb(x, y):
            pref.append((dx, dy))

    # 2) d 유지 후보
    keep = []
    for dx, dy in [(cx, -cy), (-cx, cy), (-cx, 0), (0, -cy)]:
        if (dx, dy) == (0, 0) or (dx, dy) in pref:
            continue
        if cheb(x + dx, y + dy) == cheb(x, y):
            keep.append((dx, dy))

    # 3) d 증가 후보 (막혔을 때 최후 수단) — DIRS로만 순회!
    inc = []
    for key, (dx, dy) in DIRS:
        if (dx, dy) == (0, 0) or (dx, dy) in pref or (dx, dy) in keep:
            continue
        if cheb(x + dx, y + dy) > cheb(x, y):
            inc.append((dx, dy))

    # (dx,dy) → (key,(nx,ny))로 변환
    out = []
    for dx, dy in (pref + keep + inc):
        key = DELTA_TO_KEY[(dx, dy)]
        out.append((key, (x + dx, y + dy)))
    return out

while remaining > 0:
    occ_now = occupied_now()

    # 이번 틱 (0,0) 입장 1명 선정: d==1 중 idx 작은 순
    candidates_enter = [h for h in heroes if (not h['done']) and cheb(h['x'], h['y']) == 1]
    candidates_enter.sort(key=lambda h: (h['idx']))
    entering_id = candidates_enter[0]['idx'] if candidates_enter else None

    next_choice = {}   # idx -> (key, (nx,ny))
    next_pos_map = {}  # (nx,ny) -> idx (원점 제외)
    desire_swap = {}   # idx -> (nx,ny)

    # 처리 순서: d 작은 순, idx 작은 순
    order = [h for h in heroes if not h['done']]
    order.sort(key=lambda h: (cheb(h['x'], h['y']), h['idx']))

    for h in order:
        idx = h['idx']
        x, y = h['x'], h['y']
        if (x, y) == (0, 0):
            h['done'] = True
            remaining -= 1
            continue

        entering_now = (entering_id == idx)
        forbid_origin = (cheb(x, y) == 1 and not entering_now)

        cand = candidates_for(h, entering_now=entering_now)

        picked = None
        for key, (nx, ny) in cand:
            # (0,0) 처리
            if (nx, ny) == (0, 0) and not entering_now:
                continue
            # 자기 재방문 금지
            if (nx, ny) in h['visited']:
                continue
            # 원점 외 동시점유 금지
            if (nx, ny) != (0, 0) and (nx, ny) in next_pos_map:
                continue

            # 스왑 허용 체크: (nx,ny)에 현재 다른 용사가 있고, 그가 (x,y)로 오려하면 허용
            swap_ok = False
            if (nx, ny) in occ_now:
                other_id = occ_now[(nx, ny)]
                if other_id in desire_swap and desire_swap[other_id] == (x, y):
                    swap_ok = True

            # 다른 이가 같은 칸으로 오려는 충돌(원점 제외)
            if not swap_ok and (nx, ny) != (0, 0) and (nx, ny) in desire_swap.values():
                continue

            # d==1인데 이번 차례 아니면 원점 금지
            if forbid_origin and (nx, ny) == (0, 0):
                continue

            picked = (key, (nx, ny), swap_ok)
            break

        # 그래도 못 찾으면 — 임시 한 칸 (충돌/재방문/원점 피해서)
        if picked is None:
            for key2, (dx, dy) in DIRS:
                nx, ny = x + dx, y + dy
                if (nx, ny) == (0, 0):
                    continue
                if (nx, ny) in h['visited']:
                    continue
                if (nx, ny) in next_pos_map:
                    continue
                picked = (key2, (nx, ny), False)
                break

        # 정말 없을 리는 거의 없지만, 안전장치
        if picked is None:
            dx = -sign(x) or 1
            dy = -sign(y) or 1
            key2 = DELTA_TO_KEY[(dx, dy)]
            nx, ny = x + dx, y + dy
            picked = (key2, (nx, ny), False)

        key, (nx, ny), swap_ok = picked
        next_choice[idx] = (key, (nx, ny))
        desire_swap[idx] = (nx, ny)
        if (nx, ny) != (0, 0):
            next_pos_map[(nx, ny)] = idx

    # 이동 실행
    for h in order:
        idx = h['idx']
        key, (nx, ny) = next_choice[idx]
        h['instr'].append(key)
        h['x'], h['y'] = nx, ny
        h['visited'].add((nx, ny))
        if (nx, ny) == (0, 0):
            h['done'] = True
            remaining -= 1

# 출력: 입력 순서대로
heroes.sort(key=lambda h: h['idx'])
for h in heroes:
    print(''.join(h['instr']))
