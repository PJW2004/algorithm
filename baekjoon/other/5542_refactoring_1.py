import sys

data = sys.stdin.buffer.read().splitlines()
t = int(data[0])

# bytes 기반 처리: strip + lower를 bytes 메서드로 수행
out = []
append = out.append
for i in range(1, t + 1):
    append(data[i].strip().lower())

sys.stdout.buffer.write(b"\n".join(out))
