# Hell of Optimizing Geometric Construction
# 구현: 빗변 길이(제곱) 오름차순 (dx,dy) 벡터 -> 지그재그 경로
# - 좌표 범위: [-1000, 1000]^2
# - 모든 변 길이 단조 증가 (동일 빗변 길이 제거)
# - x/y 경계에서 방향 반전 (bouncing)으로 범위 유지
# - 자동 검증 포함
#
# Python 3.x

import sys

XMIN, XMAX = -1000, 1000
YMIN, YMAX = -1000, 1000

def build_vectors(limit_i=78, limit_j=25):
    # (dx,dy) = (min(i,j), max(i,j)), i in [0,limit_i-1], j in [1,limit_j-1]
    # sort by hyp2 = i^2 + j^2, and keep only one per hyp2 (strictly increasing edge lengths)
    seen_hyp2 = set()
    vecs = []
    for i in range(limit_i):
        for j in range(1, limit_j):
            dx = min(i, j)
            dy = max(i, j)
            if dx == 0 and dy == 0:
                continue
            hyp2 = i*i + j*j
            if hyp2 in seen_hyp2:
                continue
            seen_hyp2.add(hyp2)
            vecs.append((hyp2, dx, dy))
    vecs.sort()  # by hyp2
    return [(dx,dy) for _,dx,dy in vecs]

def sqdist(a,b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def nearest_unique(points, i):
    best = None
    bestd = None
    for j in range(len(points)):
        if j == i: continue
        d = sqdist(points[i], points[j])
        if best is None or d < bestd:
            best, bestd = j, d
        elif d == bestd:
            return None, None
    return best, bestd

def verify(points):
    # 1) 좌표 중복 없음
    if len(set(points)) != len(points):
        return False, "동일 좌표 중복 발생"
    n = len(points)
    # 2) 모든 점에서 최근접 유일
    nxt = [None]*n
    for i in range(n):
        j,_ = nearest_unique(points, i)
        if j is None:
            return False, f"{i+1}번 점: 최근접 유일 아님(동점)"
        nxt[i] = j
    # 3) p 시퀀스가 [1..n]의 순열인지 확인 (1-based: start at index 0)
    seen = [False]*n
    cur = 0
    for _ in range(n):
        if seen[cur]:
            return False, "체인 중간 재방문 발생"
        seen[cur] = True
        cur = nxt[cur]
    if not all(seen):
        return False, "모든 점을 정확히 한 번씩 방문하지 않음"
    return True, "OK"

def clamp_bounce(pos, step, lo, hi, sign):
    """
    pos에서 sign*(step) 이동이 범위를 넘으면 sign을 뒤집어 bounce.
    (한 번의 반전으로 충분함: step <= 77, 범위는 2001)
    반환: new_pos, new_sign
    """
    nxt = pos + sign*step
    if nxt < lo or nxt > hi:
        sign *= -1
        nxt = pos + sign*step
    return nxt, sign

def tiny_nudge(points, i, tried=set()):
    """
    극히 드문 경우 비인접점이 더 가까워지는 엣지 케이스가 생기면
    인접성/유일성을 해치지 않는 범위에서 y를 +/-1로 미세조정.
    (정수 좌표 유지, 범위 유지)
    """
    if i in tried:  # 같은 지점에 반복 적용 방지
        return points[i]
    tried.add(i)
    x,y = points[i]
    # 가능한 4개 후보 중 범위 안인 걸로 시도
    for dy in (1,-1,2,-2):
        ny = y + dy
        if YMIN <= ny <= YMAX:
            return (x, ny)
    return (x, y)

def generate(n):
    vecs = build_vectors(78, 25)  # 약 1500개 근처, 중복 제거 후도 1320개 이상 확보
    need = n - 1
    if need > len(vecs):
        raise ValueError("벡터가 부족합니다. limit_i/j를 키우세요.")
    vecs = vecs[:need]  # 앞에서부터 거리 단조 증가로 사용

    pts = []
    x, y = -1000, -1000
    pts.append((x,y))

    sign_h = 1  # x 진행 방향 (+1/-1)
    sign_v = 1  # y 진행 방향 (+1/-1)

    for (dx,dy) in vecs:
        # 먼저 y를 bounce 규칙으로
        y, sign_v = clamp_bounce(y, dy, YMIN, YMAX, sign_v)
        # 그 다음 x를 bounce 규칙으로
        x, sign_h = clamp_bounce(x, dx, XMIN, XMAX, sign_h)
        pts.append((x,y))

    # 매우 드문 케이스용: 유일성/인접성 깨질 때 미세 보정
    # (보정이 필요 없는 게 정상이며, 필요 시에도 y +/-1만 건드림)
    ok, _ = verify(pts)
    if not ok:
        # 한 번 스윕하며, 최근접 유일성 위반 지점을 미세조정
        for i in range(n):
            j,_ = nearest_unique(pts, i)
            if j is None:
                pts[i] = tiny_nudge(pts, i)
        # 최종 재검증 (여전히 안 되면 파라미터 키우라는 메시지)
        ok2, msg2 = verify(pts)
        if not ok2:
            raise RuntimeError(f"생성/보정 실패: {msg2}")

    return pts


n = int(input())

pts = generate(n)
ok, msg = verify(pts)
print(f"[검증] {msg}", file=sys.stderr)
for x,y in pts:
    print(x, y)

