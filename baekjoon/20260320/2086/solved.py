# 피보나치 수열의 a번째부터 b번째까지의 합
# 결과는 1,000,000,000으로 나눈 나머지
# (1 <= a <= b <= 9,000,000,000,000,000,000)

import sys
input = sys.stdin.readline

MOD = 1_000_000_000

# b 최대 9*10^18
def mat_mul(A,B):
    """
    2x2 행렬 곱셈 (mod 연산 포함)

    A = [[a, b], [c, d]]
    B = [[e, f], [g, h]]
    
    결과 = [[a*e + b*g,  a*f + b*h],
            [c*e + d*g,  c*f + d*h]]
    """
    return [
        [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
         (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
         (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]
    ]
 
 
def mat_pow(M, n):
    """
    행렬 M의 n제곱을 O(log n)에 계산한다.
    
    [반복 제곱법 시뮬레이션 예시: M^13]
    
    13 = 1101₂
    
    비트 0 (값=1): result *= base(=M)      > result = M^1
    비트 1 (값=0): skip                     > result = M^1      (base = M^2)
    비트 2 (값=1): result *= base(=M^4)     > result = M^5      (base = M^4)
    비트 3 (값=1): result *= base(=M^8)     > result = M^13     (base = M^8)
    
    총 4번의 제곱 + 3번의 곱 = 7번의 행렬 곱으로 M^13 완성!
    """
    # 단위행렬 (항등원): I * A = A * I = A
    result = [[1, 0],
              [0, 1]]
    
    base = [row[:] for row in M]  # M의 복사본
    
    while n > 0:
        if n % 2 == 1:  # 현재 비트가 1이면
            result = mat_mul(result, base)  # result에 곱하기
        base = mat_mul(base, base)  # base를 제곱 (M > M^2 > M^4 > ...)
        n //= 2  # 다음 비트로
    
    return result

def fibonacci(n):
    """
    n번째 피보나치 수를 O(log n)에 계산한다.
    F(1) = 1, F(2) = 1, F(n) = F(n-1) + F(n-2)
    
    행렬 공식: [[1,1],[1,0]]^n 의 [0][1] 위치 = F(n)
    
    특수 케이스:
      n = 0 > F(0) = 0
      n = 1 > F(1) = 1
      n = 2 > F(2) = 1
    """
    if n <= 0:
        return 0
    if n <= 2:
        return 1
    
    M = [[1, 1],
         [1, 0]]
    
    result = mat_pow(M, n)
    
    # M^n = [[F(n+1), F(n)],
    #        [F(n),   F(n-1)]]
    # 따라서 F(n) = result[0][1]
    return result[0][1]

a, b = map(int, input().split())
 
# F(b+2) - F(a+1) mod 10^9
fb2 = fibonacci(b + 2)
fa1 = fibonacci(a + 1)
 
# 음수 방지를 위해 MOD를 더한 뒤 나머지
answer = (fb2 - fa1 + MOD) % MOD
 
print(answer)