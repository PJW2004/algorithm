# 준민이가 가지고 있는 빈 병의 수
# 그날 발견한 빈 병의 수
# 새 병으로 바꾸는데 필요한 빈 병의 개수

# 예시 ) 9 0 3
# 9 + 0 = 9
# 9 // 3 = 3
# 3 // 3 = 1
# 3 + 1 = 4

e,f,c = map(int,input().split())
bottle = e+f
_water = []
while bottle > c:
    temp = bottle % c
    bottle //= c
    _water.append(bottle)
    bottle += temp
if bottle == c:
    print(sum(_water)+1)
else:
    print(sum(_water))