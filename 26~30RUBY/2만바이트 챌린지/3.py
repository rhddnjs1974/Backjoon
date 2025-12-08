# challenge3.out 생성 (바이트 일치 규격: 1024줄, 각 줄 오른쪽 공백 제거 후 개행)
import sys

H, W = 1024, 2048
buf = [bytearray(b" " * W) for _ in range(H)]

# (center c, size s, step t)
peaks = [(1024, 512, 0)]  # 첫 줄은 바로 "/\"가 되도록 t=0에서 시작

for r in range(H):
    # 그리기: 각 피크는 '/  ...  \' 형태로 한 줄에 하나씩 외곽선을 확장
    row = buf[r]
    for (c, s, t) in peaks:
        L = c - 1 - t
        R = c + t
        if 0 <= L < W: row[L] = ord('/')
        if 0 <= R < W: row[R] = ord('\\')

    # 다음 줄 피크 상태 갱신
    nxt = []
    for (c, s, t) in peaks:
        if t + 1 < s:
            nxt.append((c, s, t + 1))        # 계속 벌어짐
        elif s > 1:
            h = s // 2                        # 임계 도달 → 둘로 갈라짐
            nxt.append((c - h, h, 0))         # 왼쪽 새 피크
            nxt.append((c + h, h, 0))         # 오른쪽 새 피크
        # s==1이고 t==0이었던 피크는 여기서 소멸(더 갈라지지 않음)
    peaks = nxt

# 출력: 줄마다 우측 공백 제거 후 개행(원본과 동일한 포맷)
w = sys.stdout.write
for row in buf[:3]:
    w(bytes(row).rstrip().decode('latin1') + "\n")
