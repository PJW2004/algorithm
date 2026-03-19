# 2 | 24 18
#   | -----
# 3 | 12 9
#   | -----
#     4 3
quotient_list = 1
x,y = map(int, input().split())
# from time import sleep
while x != 1 and y != 1:
    number = 2
    # 숫자 구하는 쪽
    while (x % number != 0) or (y % number != 0):
        if number == min(x,y):
            # 17 | 34 17
            #    | -----
            #      2 1
            number = 0
            break
        number += 1
        # print(y % number)
        # print(x % number)
        # print(number)
        # sleep(1)
    if number == 0:
        break
    quotient_list *= number
    x //= number
    y //= number
print(quotient_list)
print(quotient_list * x * y)