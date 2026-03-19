
# M = 6
# {1,2,3,4}, {1,2,3,5}, {1,2,3,6}
# {1,2,4,5}, {1,2,4,6}
# {1,2,5,6}
# {1,3,4,5}, {1,3,4,6}
# {1,3,5,6}
# {1,4,5,6}
# {2,3,4,5}
for _ in range(int(input())):
    N, M = map(int, input().split())
    if N == 1:
        print(M)
        continue
    numerator = 1   # 분자
    for k in range(N):
        # sigma_M=0^k = (M-k)
        numerator *= M-k
    denominator = 1 # 분모
    for k in range(N,0,-1): # 팩토리얼
        denominator *= k
    print(numerator // denominator)