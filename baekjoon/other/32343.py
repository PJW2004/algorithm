import sys
stdin = sys.stdin

n = int(stdin.readline().strip()) # -> n 자리 이진수
a,b = map(int, stdin.readline().split())

overlap = max(0, a + b - n)        # 둘 다 1일 수밖에 없는 자리 수
diff    = a + b - 2 * overlap      # XOR가 1이 되는 자리 수

if diff == 0:                      # 모든 비트에서 값이 같을 때
    print(0)
else:
    # 2^n - 2^(n - diff)  ==  (1 << n) - (1 << (n - diff))
    print((1 << n) - (1 << (n - diff)))