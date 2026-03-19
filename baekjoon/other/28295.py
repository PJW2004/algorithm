# t = 1 이면 우향우
# t = 2 이면 뒤로 돌아
# t = 3 이면 좌향좌

# 우향우: 각 학생은 현재 상태에서 오른쪽으로 90도 돈다.
# 뒤로 돌아: 각 학생은 현재 상태에서 오른쪽으로 180도 돈다.
# 좌향좌: 각 학생은 현재 상태에서 왼쪽으로 90도 돈다.

# 북쪽 : N
# 동쪽 : E
# 서쪽 : W
# 남쪽 : S

# 초기에 북쪽
command = 0
for _ in range(10):
    match int(input()):
        case 1: # 우향우
            command += 90
        case 2: # 뒤로 돌아
            command += 180
        case 3: # 좌향좌
            command -= 90
coordinate = command % 360
if coordinate < 90: # 북쪽
    print('N')
elif coordinate < 180: # 동쪽
    print('E')
elif coordinate < 270: # 남쪽
    print('S')
else: # 서쪽
    print('W')