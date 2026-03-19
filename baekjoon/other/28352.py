# 10 <= N <= 17 
# 60(초) * 60(분) * 24(시) = 86,400(초)
# 1 주에 7일 = 604,800(초)
# def factorial(number:int):
#     if number == 0:
#         return 1
#     return number * factorial(number-1)

# # 6
# # 66
# # 792
# # 10296
# # 144144
# # 2162160
# # 34594560
# # 588107520
# for number in range(10, 18):
#     print(factorial(number)//604_800)

import sys
match int(sys.stdin.readline()):
    case 10:
        print('6')
    case 11:
        print('66')
    case 12:
        print('792')
    case 13:
        print('10296')
    case 14:
        print('144144')
    case 15:
        print('2162160')
    case 16:
        print('34594560')
    case 17:
        print('588107520')