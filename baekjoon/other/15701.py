# 10 -> (1,10), (10,1), (2,5), (5,2)
# 16 -> (1,16), (16,1), (4,4), (2,8), (8,2)
# 이 문제는 약수 구하기.
# 소인수 분해를 해야하나.
# number = int(input())
# prime_factorization = {}
# while number != 1:
#     for _number in range(2, number+1):
#         print(_number)
#         if number % _number == 0:
#             if prime_factorization.get(_number, None) == None:
#                 prime_factorization[_number] = 1
#             else:
#                 prime_factorization[_number] += 1
#             number = number // _number
#             break
# print(prime_factorization)
    

import math

def factor_pairs(n: int, ordered: bool = True):
    pairs = []
    r = math.isqrt(n)  # floor(sqrt(n))
    for d in range(1, r + 1):
        if n % d == 0:
            e = n // d
            pairs.append((d, e))
            if ordered and d != e:
                pairs.append((e, d))
    return pairs

# 예시
# n = 469_762_049
# n = 16
pairs = factor_pairs(int(input()), ordered=True)
print(len(pairs))