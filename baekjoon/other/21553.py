# A는 P를 부분 문자열로 가진다.
# A, P의 모든 문자는 1이상 9이하의 숫자이다.
# K = |P|
# |B| <= 100
# P가 유일한 비밀번호가 되게 하는 B를 아무거나 출력한다.
# string_a = input()
# password = input()
# number_list = set([1,2,3,4,5,6,7,8,9]) - set(map(int, list(string_a)))
# string_b = password
# while 1:
#     # 애드훅 문제라니요.
#     if int(string_b) >= 100:
#         break
#     answer = ""
#     for number in number_list:
#         temp_string_b = string_b + str(number)
#         if int(temp_string_b) < 100:
#             continue
#         if temp_string_b in string_a:
#             continue
#         answer = str(number)
#     if answer:
#         string_b += answer
# print(string_b)
import sys

_ = sys.stdin.readline().strip()  # A (사용하지 않음)
P = sys.stdin.readline().strip()  # 비밀번호 후보
print(P)