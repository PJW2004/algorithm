# 6-bit decoder, ultra-tight:
# - no string compare, use (byte & 1) to get bit
# - fixed-length slice, no strip
# - prealloc output, bytes LUT, single buffered write

import sys

data = open(0, 'rb').read()
nl = data.find(b'\n')
n = int(data[:nl])
s = data[nl+1:nl+1+6*n]  # 정확히 6*n 바이트만 사용

# 패턴(정수) 준비
pats = (0b000000, 0b001111, 0b010011, 0b011100,
        0b100110, 0b101001, 0b110101, 0b111010)

# 64칸 LUT: 0=불일치, 그 외엔 'A'..'H' ASCII
lut = bytearray(64)
for idx, p in enumerate(pats):
    ch = 65 + idx  # 'A'..'H'
    lut[p] = ch
    lut[p ^ 1]  = lut[p ^ 1]  or ch
    lut[p ^ 2]  = lut[p ^ 2]  or ch
    lut[p ^ 4]  = lut[p ^ 4]  or ch
    lut[p ^ 8]  = lut[p ^ 8]  or ch
    lut[p ^ 16] = lut[p ^ 16] or ch
    lut[p ^ 32] = lut[p ^ 32] or ch
lut = bytes(lut)  # 읽기 전용 bytes로 고정 (인덱싱 빠름)

# 디코딩
out = bytearray(n)
dec = lut  # 로컬 바인딩
idx = 0
oi = 0
limit = 6 * n

# 로컬 변수로 잡아서 전역 조회 비용 최소화
s0 = s  # 로컬 alias

while idx < limit:
    # '0'==48, '1'==49 -> &1 로 0/1 추출 (비교/분기 없음)
    code = ((s0[idx]   & 1) << 5) | ((s0[idx+1] & 1) << 4) | \
           ((s0[idx+2] & 1) << 3) | ((s0[idx+3] & 1) << 2) | \
           ((s0[idx+4] & 1) << 1) |  (s0[idx+5] & 1)

    ch = dec[code]
    if ch == 0:  # 2비트 이상 오류
        # i번째(1-based) 조각 번호 출력
        sys.stdout.write(str(idx // 6 + 1))
        sys.exit(0)

    out[oi] = ch
    oi += 1
    idx += 6

sys.stdout.buffer.write(out)
