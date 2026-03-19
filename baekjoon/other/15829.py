# 자주 쓰이는 방식인가보네. 기억하라고 강조하시는거 보면.
# 알파벳은 소문자만 나온다.
# 'a' = 97
# 'z' = 122
l = int(input())
m = 1234567891 # 놀랍게도 소수라고 하심.
alphabet = input()
output = 0
for i, character in enumerate(alphabet):
    data = ord(character) - 96
    data *= 31**i
    output += data
# M 으로 나눈 나머지도 잊지 말기.
print(output % m)