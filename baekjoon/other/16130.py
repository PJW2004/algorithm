# 0~9 는 그대로
# A~Z 는 10~35

# SK -> 28 = 2, 48 = 4
# print(ord('S')-55)
# print(ord('K')-55)
# 몫이 1,2,3 인 겨우 1,2,3 주 퇴사
# 4인 경우 (weapon)
# 4보다 큰 경우 (09)

import sys

for _ in range(int(sys.stdin.readline())):
    string_list = sys.stdin.readline().strip()
    output = ""
    demerit = 0
    quit_count = 0
    temp = 0
    for string in string_list:
        if string.isdigit():
            # 4
            # 7 -> 11 = 퇴사 += 1
            # 9 -> 20
            # 6 -> 26 = 퇴사 += 2
            # : 3
            demerit += int(string)
        else:
            demerit += ord(string) - 55
        quit = demerit // 10
        if quit == temp:
            continue
        temp = quit
        if quit == 4:
            output = "(weapon)"
            break
        elif quit > 4:
            output = "(09)"
            break
        quit_count += quit
    print(f"{quit_count}{output}")