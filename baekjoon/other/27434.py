def factorial(number:int) -> int:
    # 재귀 사용하면 RecursionError 발생
    # 2000 부터
    # if number > 0:
    #     return number * factorial(number - 1)
    # else:
    #     return 1
    answer = 1
    for index in range(2, number + 1):
        answer *= index
    return answer
import sys
# input 은 4300 digits 걸림.
# print(factorial(int(input())))
# Python 3.11+ 자릿수 제한 해제 (안전하게)
if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)
import math
# print(factorial(int(sys.stdin.readline().strip())))
print(math.factorial(int(sys.stdin.readline().strip())))