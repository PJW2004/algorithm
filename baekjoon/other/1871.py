# 첫 번째 부분의 가치와 두 번째 부분의 가치의 차이가 100을 넘지 않는 번호판
# A (65) ~ Z (90)
for _ in range(int(input())):
    content,number=input().split('-')
    value:int = sum([(ord(character) - 65)*(26**(2-index)) for index, character in enumerate(content)])
    if abs(value - int(number)) < 101:
        print("nice")
    else:
        print("not nice")