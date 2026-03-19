# 이모지의 난이도 공식
# (이모지의 전 길이) + (콜론의 개수) + (언더바의 개수) * 5
imoge = input()
print(len(imoge) + imoge.count(':') + imoge.count('_') * 5)