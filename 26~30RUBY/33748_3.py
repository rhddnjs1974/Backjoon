# Hell of Optimizing Geometric Construction
# 규칙 구현:
#  - 세로(컬럼): (dx,dy)=(min,max), x는 [L,L+25] 안에서만 ±dx, y는 한 방향으로만 ±dy
#  - 천장/바닥 도달 시: 가로(우측) 구간으로 전환, y=0, x += H (정수)
#      * H = floor(L*) where L*는 "직전에 쓴 길이보다 작은 길이들" 중 최대
#      * x+H <= XMAX-25 를 만족하는 H만 사용 (없으면 그보다 작은 길이 탐색)
#      * 이 H를 쓴 시점부터 "길이 > H"인 후보들은 전부 버림 (다음 세로는 < H만)
#  - 모든 좌표는 정수, [-1000,1000]^2 유지
#  - 생성 후: 유일 최근접 + p-체인 검증
#
# Python 3.x

import sys
import math

XMIN, XMAX = -1000, 1000
YMIN, YMAX = -1000, 1000
BAND_W = 40   # per-column width

def build_lengths(limit_i=78, limit_j=25):
    """고유한 길이 L = sqrt(i^2 + j^2) (i in [0..77], j in [1..24])와 그 (dx,dy)=(min,max) 반환.
       길이는 내림차순으로 정렬."""
    seen = set()
    items = []
    for i in range(limit_i):
        for j in range(1, limit_j):
            h2 = i*i + j*j
            if h2 == 0 or h2 in seen:
                continue
            seen.add(h2)
            dx = min(i, j)
            dy = max(i, j)
            L = math.sqrt(h2)
            items.append((L, dx, dy))
    items.sort(reverse=True, key=lambda t: t[0])  # 길이 큰 것부터
    return items  # list of (L, dx, dy)

def sqd(a,b): return (a[0]-b[0])**2 + (a[1]-b[1])**2

def nearest_unique(P, i):
    best = None; bd=None
    for j in range(len(P)):
        if j == i: continue
        d = sqd(P[i], P[j])
        if bd is None or d < bd: best=j; bd=d
        elif d == bd: return None, None
    return best, bd

def verify(P):
    n = len(P)
    if len(set(P)) != n:
        return False, "좌표 중복"
    nxt = [None]*n
    for i in range(n):
        j,_ = nearest_unique(P, i)
        if j is None:
            return False, f"{i+1}번: 최근접 유일 아님"
        nxt[i] = j
    seen = [False]*n
    cur = 0
    for _ in range(n):
        if seen[cur]: return False, "체인 재방문"
        seen[cur] = True
        cur = nxt[cur]
    if not all(seen): return False, "모든 점 미방문"
    return True, "OK"

def choose_sx_in_band(x, dx, Lleft):
    """세로 구간에서 x를 [Lleft, Lleft+BAND_W] 안에 남기기 위해 sx 선택."""
    if Lleft <= x + dx <= Lleft + BAND_W: return +1
    if Lleft <= x - dx <= Lleft + BAND_W: return -1
    # 이론상 dx<=24, BAND_W=25라 항상 하나는 있음. 안전장치:
    # 더 가까운 쪽으로.
    mid = Lleft + BAND_W/2
    return +1 if abs((x+dx)-mid) < abs((x-dx)-mid) else -1

def generate(n):
    need = n - 1
    items = build_lengths(80, 40)  # (L, dx, dy), L 내림차순
    if need > len(items):
        raise ValueError("길이 후보가 부족합니다. limit_i/j를 늘리세요.")

    # 사용 가능 구간 [0..avail_end] (길이 엄격 감소 유지용)
    avail_end = 0  # 아직 아무 것도 안 썼으니 제일 큰 것부터 가능
    # 전략상 우리는 "항상 가장 큰 가능 길이"를 쓰므로, 포인터를 증가시켜가며 사용

    P = []
    x, y = -1000, -1000
    P.append((x,y))

    # 초기 밴드 [Lleft, Lleft+25] : 현재 x가 포함되도록
    Lleft = min(max(XMIN, x), XMAX - BAND_W)

    # 세로 진행 방향: +1(위)로 시작. 천장/바닥 걸리면 가로 전환 후 반전.
    vdir = +1

    used = 0
    last_len = float('inf')  # 직전 스텝의 길이(단조 감소 보장용)

    idx = 0  # 다음으로 고려할 "큰 길이"의 인덱스

    mode = "VERT"  # "VERT" 또는 "HORIZ_PENDING" (천장/바닥으로 세로 불가→가로로 전환)
    while used < need:
        if mode == "VERT":
            # 가장 큰 길이부터 순서대로 보되, last_len보다 작은 것 중에서 "세로로 실제 이동 가능한" 것을 고른다.
            found = False
            while idx < len(items):
                L, dx, dy = items[idx]
                if L >= last_len:
                    idx += 1
                    continue
                # 세로 한 방향(vdir)으로 진행 가능?
                ny = y + vdir*dy
                if ny < YMIN or ny > YMAX:
                    # 천장/바닥에 걸림 → 이번엔 세로 스텝 금지, 가로 전환으로 넘어감
                    mode = "HORIZ_PENDING"
                    found = False
                    break
                # 세로 가능: x는 밴드 안으로 ±dx만큼
                sx = choose_sx_in_band(x, dx, Lleft)
                nx = x + sx*dx
                # 밴드 벗어나면(이론상 없지만) 다음 후보 보거나 안전장치로 sx 반대로 한 번 더 확인
                if not (Lleft <= nx <= Lleft + BAND_W):
                    sx = -sx
                    nx = x + sx*dx
                    if not (Lleft <= nx <= Lleft + BAND_W):
                        idx += 1
                        continue
                # 적용
                x, y = nx, ny
                P.append((x,y))
                used += 1
                last_len = L
                idx += 1
                found = True
                break

            if mode == "HORIZ_PENDING":
                # 바로 가로 단계로 넘어감 (이번 루프에서 처리)
                continue

            if not found and mode == "VERT":
                # 더는 세로도 고를 수 없으면 가로 전환 필요
                mode = "HORIZ_PENDING"
                continue

        if mode == "HORIZ_PENDING":
            # 가로 이동: y변화=0, x증가=H (정수).
            # 규칙: H는 "직전 length(last_len)"보다 작은 길이들 중 최대를 고른 뒤 floor로 정수화,
            # 그리고 x+H <= XMAX-25 를 만족해야 함. 그런 길이가 없으면 그 아래 길이들 중에서 찾는다.
            h_found = False
            # 수색 포인터: (last_len보다 작은 구간 중 최대) ⇒ idx가 가리키는 곳부터 내려갈 필요 없이,
            # 이미 idx는 last_len보다 작은 것들을 가리키고 있음. 그중 가장 큰 것부터 시도.
            h_idx = idx
            best_h = None
            while h_idx < len(items):
                Lh, dxh, dyh = items[h_idx]
                if Lh >= last_len:  # 더 큰 길이는 못 씀
                    h_idx += 1
                    continue
                H = math.floor(Lh)  # 정수 x이동
                if H <= 0:
                    h_idx += 1
                    continue
                # 새 밴드 왼쪽 경계 = x+H 가 되어야 하므로, x+H <= XMAX-25
                if x + H <= XMAX - BAND_W:
                    best_h = (h_idx, Lh, H)
                    break
                # 너무 커서 오른쪽 끝 넘김 → 더 작은 길이 시도
                h_idx += 1

            if best_h is None:
                raise RuntimeError("가로 전환을 위한 유효한 H를 찾지 못했습니다. (박스 오른쪽 끝)")

            _, Lh, H = best_h
            # 가로 이동 적용
            x = x + H  # 오른쪽으로만
            # y는 변화 없음

            P.append((x, y))
            used += 1

            # 새 밴드 지정: [x, x+25]
            Lleft = x  # 명시적으로 '왼쪽 경계 = 현재 x'
            # 다음 세로는 "길이 < H"만 허용(규칙: X축 이동에 쓴 값보다 큰 길이는 버리기)
            last_len = H

            # 세로 진행방향 반전
            vdir *= -1

            mode = "VERT"
            # idx는 그대로 두되(last_len 조건이 걸러준다), 계속 last_len보다 작은 항목만 사용할 것



    return P

n = int(input())
pts = generate(n)
ok, msg = verify(pts)
print(f"[검증] {msg}", file=sys.stderr)
for x,y in pts:
    print(x, y)

