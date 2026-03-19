# L 이상 U 이하 모든 정수의 각 자리 합
# 0 <= L <= U <= 2,000,000,000

import sys
input = sys.stdin.readline

def sum_digit_sums(n):
    """
    0부터 n까지 모든 수의 자릿수 합의 총합을 구한다.
    f(n) = digitsum(0) + digitsum(1) + ... + digitsum(n)
    
    각 자릿수 위치 p(0=1의자리, 1=10의자리, ...)에 대해
    해당 위치의 총 기여도를 독립적으로 계산한다.
    
    시간복잡도: O(자릿수 개수) = O(log n)
    """
    if n < 0:
        return 0
    
    total = 0
    power = 1  # 10^p, p=0부터 시작
    
    while power <= n:
        # N을 위치 p 기준으로 분해
        higher = n // (power * 10)   # p 위의 자릿수들
        current = (n // power) % 10  # p 위치의 자릿수
        lower = n % power            # p 아래의 자릿수들
        
        # 항1: 완전 순환 기여
        # higher번의 0~9 완전 순환, 0+1+...+9 = 45
        total += higher * 45 * power
        
        # 항2: 불완전 순환에서 0 ~ (current-1) 기여
        # (0 + 1 + ... + (current-1)) * power = current*(current-1)/2 * power
        total += current * (current - 1) // 2 * power
        
        # 항3: current 자체의 기여
        # current는 lower+1번 등장
        total += current * (lower + 1)
        
        power *= 10  # 다음 자릿수 위치로
    
    return total

L, U = map(int, input().split())
 
# f(U) - f(L-1)
answer = sum_digit_sums(U) - sum_digit_sums(L - 1)
print(answer)