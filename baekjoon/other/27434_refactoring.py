import sys

# Python 3.11+ 긴 정수 문자열 변환 제한 완화 (필요 시)
if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(100000)

def _prod_tree(lo: int, hi: int) -> int:
    """정수 구간 [lo, hi]의 곱을 분할정복으로 계산 (lo <= hi)."""
    if lo > hi:
        return 1
    if lo == hi:
        return lo
    if hi - lo == 1:
        return lo * hi
    mid = (lo + hi) // 2
    return _prod_tree(lo, mid) * _prod_tree(mid + 1, hi)

def factorial(n: int) -> int:
    if n < 2:
        return 1
    # 2..n 구간의 곱을 product tree로 계산
    return _prod_tree(2, n)

def main():
    s = sys.stdin.readline().strip()
    n = int(s)
    print(factorial(n))

if __name__ == "__main__":
    main()
