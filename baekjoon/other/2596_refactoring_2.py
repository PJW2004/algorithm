# 32ms 나옴.
# BOJ-Style Fast Decoder (6-bit, <=1bit error allowed)
# - 전수 룩업 테이블(길이 64) 사전계산
# - sys.stdin.buffer, bytes 비교(= '1' == 49)
# - 6글자 조각을 고정식 비트 합성(루프/함수호출 제거)

import sys
rb = sys.stdin.buffer.readline
n = int(rb())
s = rb().strip()  # bytes

# 패턴을 정수(6비트)로 정의
pats = [0b000000, 0b001111, 0b010011, 0b011100,
        0b100110, 0b101001, 0b110101, 0b111010]

# 64칸 룩업: 해당 6비트가 어떤 문자(A~H)인지, 아니면 0(불일치)
decode = [0] * 64
for idx, p in enumerate(pats):
    ch = 65 + idx               # 'A'..'H' (ASCII)
    decode[p] = ch              # 완전 일치
    for b in range(6):          # 1비트 플립들도 같은 문자로 매핑
        q = p ^ (1 << b)
        if decode[q] == 0:
            decode[q] = ch

# 디코딩
out = bytearray()
ONE = 49  # ord('1')
for i in range(0, 6 * n, 6):
    # 6글자 고정 결합 (루프 없이 분기 최소화)
    code = ((s[i]   == ONE) << 5) | ((s[i+1] == ONE) << 4) | \
           ((s[i+2] == ONE) << 3) | ((s[i+3] == ONE) << 2) | \
           ((s[i+4] == ONE) << 1) |  (s[i+5] == ONE)

    ch = decode[code]
    if ch == 0:                 # 2비트 이상 오류
        print(i // 6 + 1)
        sys.exit(0)

    out.append(ch)

sys.stdout.write(out.decode())
