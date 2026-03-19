"""
- 비밀번호는 알파벳 소문자, 대문자, 숫자, 특수문자로만 이루어져 있다.
- 비밀번호는 6글자 이상이어야 한다.
- 숫자는 하나 이상 포함되어야 한다.
- 알파벳 소문자는 하나 이상 포함되어야 한다.
- 알파벳 대문자는 하나 이상 포함되어야 한다.
- 특수 문자는 하나 이상 포함되어야 한다. 사용할 수 있는 특수 문자는 !@#$%^&*()-+이다.
"""
n = int(input())
string=input()
# 특수 문자.
special_ascii=[
    33, # !
    64, # @
    35, # #
    36, # $
    37, # %
    94, # ^
    38, # &
    42, # *
    40, # (
    41, # )
    45, # -
    43  # +
]
# o(string) * 4
# counting=0
# if n < 6:
#     counting+=1
# # 숫자 판별
# if len([1 for character in string if character.isdecimal()]) < 1:
#     counting+=1
# # 대문자 판별 (A-B)
# if len([1 for character in string if 64 < ord(character) < 91]) < 1:
#     counting+=1
# # 소문자 판별 (a-b)
# if len([1 for character in string if 96 < ord(character) < 123]) < 1:
#     counting+=1
# # 특수문자 판별
# if len([1 for character in string if ord(character) in special_ascii]) < 1:
#     counting+=1

# 비밀번호는 6글자 이상이어야 한다.
if len(string) > 5:
    check_length=True
else:
    check_length=False
check_decimal=False
check_upper=False
check_lower=False
check_special=False
for character in string:
    # 숫자는 하나 이상 포함되어야 한다.
    if character.isdecimal():
        check_decimal=True
        continue
    character_ascii:int = ord(character)
    # 알파벳 대문자는 하나 이상 포함되어야 한다.
    if 64 < character_ascii < 91:
        check_upper=True
        continue
    # 알파벳 대문자는 하나 이상 포함되어야 한다.
    elif 96 < character_ascii < 123:
        check_lower=True
        continue
    # 특수 문자는 하나 이상 포함되어야 한다. 사용할 수 있는 특수 문자는 !@#$%^&*()-+이다.
    elif character_ascii in special_ascii:
        check_special=True
        continue
# sum 으로 True 값만 개수 확인.
missing_classes = 4 - sum([check_decimal, check_upper, check_lower, check_special])
# 전체 길이 간격을 채운 다음, 그 간격의 최대값과 누락된 문자 범주의 개수 구함.
missing_length  = max(0, 6 - n)
print(max(missing_classes, missing_length))