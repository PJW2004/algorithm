n = int(input())
SPECIALS = set("!@#$%^&*()-+")
password = input().rstrip()   # 개행 제거

# 각 클래스 충족 여부
has_digit   = any(character.isdigit()   for character in password)
has_lower   = any(character.islower()   for character in password)
has_upper   = any(character.isupper()   for character in password)
has_special = any(character in SPECIALS for character in password)

missing_classes = 4 - sum((has_digit, has_lower, has_upper, has_special))
missing_length  = max(0, 6 - len(password))

print(max(missing_classes, missing_length))