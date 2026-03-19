import sys, math

it = iter(map(int, sys.stdin.buffer.read().split()))
t = next(it)

out = []
append = out.append  # 로컬 바인딩(약간의 이득)
for _ in range(t):
    N = next(it); M = next(it)
    append(str(math.comb(M, N)) if 0 <= N <= M else "0")

sys.stdout.write("\n".join(out))