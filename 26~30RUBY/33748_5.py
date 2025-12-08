# parameter_sweeper.py
# 목적: BAND_W, LIMIT_I, LIMIT_J, SEP_MIN 조합을 탐색하며
#       n <= 1320 범위에서 최대 통과 n을 찾는다.
# 사용: python3 parameter_sweeper.py
#
# 주: 이 파일 하나로 실행 가능. (표준입력 불필요)

import math
import itertools
from typing import List, Tuple

# ----- 전역 박스 -----
XMIN, XMAX = -1000, 1000
YMIN, YMAX = -1000, 1000

# ====== 길이 풀 생성 ======
def build_lengths(limit_i: int, limit_j: int) -> List[Tuple[float, int, int]]:
    """고유한 길이 L = sqrt(i^2 + j^2) 집합을 길이 내림차순으로.
       각 원소는 (L, dx=min(i,j), dy=max(i,j))."""
    seen = set()
    items = []
    for i in range(limit_i):      # i: 0..limit_i-1
        for j in range(1, limit_j):  # j: 1..limit_j-1
            h2 = i*i + j*j
            if h2 == 0 or h2 in seen:
                continue
            seen.add(h2)
            dx = min(i, j)
            dy = max(i, j)
            L = math.sqrt(h2)
            items.append((L, dx, dy))
    items.sort(reverse=True, key=lambda t: t[0])  # 길이 큰 것부터
    return items

# ====== 유틸/검증 ======
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
    #for i in range(n):
    #    j,_ = nearest_unique(P, i)
    #    if j is None:
    #        return False, f"{i+1}번: 최근접 유일 아님"
    #    nxt[i] = j
    seen = [False]*n
    cur = 0
    #for _ in range(n):
    #    if seen[cur]: return False, "체인 재방문"
    #    seen[cur] = True
    #    cur = nxt[cur]
    #if not all(seen): return False, "모든 점 미방문"
    return True, "OK"

def choose_sx_in_band(x, dx, Lleft, BAND_W):
    """세로 구간: x를 [Lleft, Lleft+BAND_W] 안에 유지하기 위해 sx 선택."""
    if Lleft <= x + dx <= Lleft + BAND_W: return +1
    if Lleft <= x - dx <= Lleft + BAND_W: return -1
    # 이론상 dx<=24/… & BAND_W>=25이면 항상 하나 존재. 안전장치(중앙 기준 가까운 쪽):
    mid = Lleft + BAND_W/2
    return +1 if abs((x+dx)-mid) < abs((x-dx)-mid) else -1

def choose_sy(y, step):
    """YMIN <= y + sy*step <= YMAX 를 만족하는 sy ∈ {+1,-1}."""
    if YMIN <= y + step <= YMAX: return +1
    if YMIN <= y - step <= YMAX: return -1
    # 높이 2001, step<=limit_j-1 (보통 <= 39/…): 항상 가능해야 함. 안전장치:
    return +1 if (y <= 0) else -1

# ====== 핵심 생성기 (네 규칙) ======
def generate(n: int, BAND_W: int, LIMIT_I: int, LIMIT_J: int, SEP_MIN: int):
    """네 규칙 구현 + 파라미터화:
       - 세로: (dx,dy)=(min,max)로 한 방향 진행. x는 현재 밴드 [L, L+BAND_W] 안으로 sx 선택.
       - 천장/바닥에 걸리면 → 가로 전환 모드(HORIZ_PENDING).
       - 가로 전환: y변화=0, x+=H(정수). H는 '직전 길이(last_len)보다 작은 길이들' 중 최대의 floor(Lh),
         그리고 x+H <= XMAX-BAND_W 를 만족해야 함. 그 이후 last_len=H로 내려앉혀 작은 길이만 사용.
       - 가로 전환이 끝나면 새 밴드 [x, x+BAND_W] 설정, 세로 진행 방향 반전.
    """
    if n < 2: return [(-1000,-1000)]
    need = n - 1

    items = build_lengths(LIMIT_I, LIMIT_J)  # (L, dx, dy) 내림차순
    if need > len(items):
        raise ValueError("길이 후보가 부족합니다. LIMIT_I/J를 늘리세요.")

    P = []
    x, y = -1000, -1000
    P.append((x,y))

    # 초기 밴드 [Lleft, Lleft+BAND_W] — 현재 x 포함
    Lleft = min(max(XMIN, x), XMAX - BAND_W)

    vdir = +1                 # 세로 진행 부호(+1 위로 시작)
    last_len = float('inf')   # 직전 간선 길이 (단조 감소 유지)
    idx = 0                   # items 인덱스(내림차순)

    mode = "VERT"             # "VERT" 또는 "HORIZ_PENDING"
    used = 0

    while used < need:
        if mode == "VERT":
            # last_len 보다 작은 길이 중에서, 실제 세로 이동 가능한 첫 항목 사용
            found = False
            while idx < len(items):
                L, dx, dy = items[idx]
                if L >= last_len:
                    idx += 1
                    continue
                sy = vdir
                # 세로 진행 가능?
                ny = y + sy*dy
                if ny < YMIN or ny > YMAX:
                    # 이번 세로 스텝 불가 → 가로 전환 모드로
                    mode = "HORIZ_PENDING"
                    found = False
                    break
                # 밴드 안으로 x 이동
                sx = choose_sx_in_band(x, dx, Lleft, BAND_W)
                nx = x + sx*dx
                if not (Lleft <= nx <= Lleft + BAND_W):
                    # 안전장치: 반대 부호 한 번 더 시도
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
                continue
            if not found:
                mode = "HORIZ_PENDING"
                continue

        if mode == "HORIZ_PENDING":
            # 가로 전환: H = floor(Lh) (Lh < last_len 중 최대) & x+H <= XMAX - BAND_W
            h_idx = idx
            bestH = None
            while h_idx < len(items):
                Lh, dxh, dyh = items[h_idx]
                if Lh >= last_len:
                    h_idx += 1
                    continue
                H = math.floor(Lh)
                if H <= 0:
                    h_idx += 1
                    continue
                # 오른쪽 끝 여유: 새 밴드 왼쪽 경계가 x+H
                if x + H <= XMAX - BAND_W:
                    bestH = (h_idx, Lh, H)
                    break
                h_idx += 1

            if bestH is None:
                # 오른쪽 끝 여유가 부족함 → 실패 리턴
                raise RuntimeError("가로 전환을 위한 유효한 H를 찾지 못했습니다. (박스 오른쪽 끝)")

            _, Lh, H = bestH
            # 가로 적용
            x = x + H       # 오른쪽으로만
            # y 변화 없음
            P.append((x, y))
            used += 1

            # 새 밴드 [x, x+BAND_W] 지정 + 세로 방향 반전
            Lleft = x
            vdir *= -1

            # 앞으로는 길이 < H 만 사용
            last_len = H
            mode = "VERT"

    # 검증
    ok, msg = verify(P)
    if not ok:
        raise RuntimeError(f"생성/검증 실패: {msg}")
    return P

# ====== 탐색기 ======
def max_n_for_params(BAND_W, LIMIT_I, LIMIT_J, SEP_MIN_dummy=0, cap=1320):
    """n=2..cap까지 순차 증가하며 최대 통과 n을 반환.
       (느리면 이진탐색으로 바꿔도 됨)"""
    # SEP_MIN은 현재 규칙엔 직접 사용하지 않지만,
    # 파라미터 그리드 일관성을 위해 인터페이스에 남겨둠.
    last_ok = 1
    for n in range(2, cap+1):
        try:
            generate(n, BAND_W, LIMIT_I, LIMIT_J, SEP_MIN_dummy)
            last_ok = n
        except Exception as e:
            return last_ok, str(e)
    return last_ok, "OK"

def try_params():
    BAND_W_list  = []
    for i in range(20,51):
        BAND_W_list.append(i)
    LIMIT_I_list = []
    for i in range(68,94):
        LIMIT_I_list.append(i)
    LIMIT_J_list = [40]
    for i in range(21,45):
        LIMIT_J_list.append(i)
    SEP_MIN_list = [30]   # 현재 구현엔 아직안씀

    results = []
    total = len(BAND_W_list)*len(LIMIT_I_list)*len(LIMIT_J_list)*len(SEP_MIN_list)
    done = 0

    for BAND_W, LIMIT_I, LIMIT_J, SEP_MIN in itertools.product(BAND_W_list, LIMIT_I_list, LIMIT_J_list, SEP_MIN_list):
        done += 1
        try:
            maxn, reason = max_n_for_params(BAND_W, LIMIT_I, LIMIT_J, SEP_MIN, cap=1320)
        except Exception as e:
            maxn, reason = 1, f"init-fail: {e}"
        results.append((maxn, BAND_W, LIMIT_I, LIMIT_J, SEP_MIN, reason))
        # 진행상황 간단히 표시
        print(f"[{done}/{total}] BAND_W={BAND_W}, I={LIMIT_I}, J={LIMIT_J}, SEP={SEP_MIN} -> max n={maxn} ({reason})")

    # 성능 좋은 조합 상위 10개 정렬 출력
    results.sort(key=lambda t: (-t[0], t[1], t[2], t[3]))
    print("\n=== Top configurations ===")
    for row in results[:10]:
        maxn, BAND_W, LIMIT_I, LIMIT_J, SEP_MIN, reason = row
        print(f"max n={maxn:4d} | BAND_W={BAND_W:2d}, I={LIMIT_I:2d}, J={LIMIT_J:2d}, SEP={SEP_MIN:2d} | note={reason}")

if __name__ == "__main__":
    try_params()






"""
max n=1214 | BAND_W=47, I=78, J=37, SEP=30 | note=가로 전환을 위한 유효한 H를 찾지 못했습니다. (박스 오른쪽 끝)
max n=1203 | BAND_W=39, I=85, J=33, SEP=30 | note=가로 전환을 위한 유효한 H를 찾지 못했습니다. (박스 오른쪽 끝)
max n=1203 | BAND_W=47, I=77, J=37, SEP=30 | note=가로 전환을 위한 유효한 H를 찾지 못했습니다. (박스 오른쪽 끝)
max n=1194 | BAND_W=50, I=73, J=44, SEP=30 | note=가로 전환을 위한 유효한 H를 찾지 못했습니다. (박스 오른쪽 끝)
max n=1191 | BAND_W=50, I=73, J=42, SEP=30 | note=가로 전환을 위한 유효한 H를 찾지 못했습니다. (박스 오른쪽 끝)
max n=1189 | BAND_W=50, I=73, J=41, SEP=30 | note=가로 전환을 위한 유효한 H를 찾지 못했습니다. (박스 오른쪽 끝)
max n=1187 | BAND_W=40, I=85, J=36, SEP=30 | note=가로 전환을 위한 유효한 H를 찾지 못했습니다. (박스 오른쪽 끝)
max n=1186 | BAND_W=43, I=78, J=37, SEP=30 | note=가로 전환을 위한 유효한 H를 찾지 못했습니다. (박스 오른쪽 끝)
max n=1185 | BAND_W=44, I=77, J=35, SEP=30 | note=가로 전환을 위한 유효한 H를 찾지 못했습니다. (박스 오른쪽 끝)
max n=1184 | BAND_W=42, I=78, J=37, SEP=30 | note=가로 전환을 위한 유효한 H를 찾지 못했습니다. (박스 오른쪽 끝)
"""