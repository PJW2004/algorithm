# 이걸 합쳐
# 일자로
# -> 10 (가로), 6 (세로), 14 (심어진 배추의 개수)
weight, hight, request_cnt = input().split(" ")
test_temp_list = [
    0 for _ in range(int(weight)) for _ in range(int(hight))
]

coordinate = [] # 좌표
for _ in range(int(request_cnt)):
    # (10,0) -> 0 번째 세로의 10 번째 가로에 배추를 심겠다.
    weight_dot, hight_dot = input().split(" ")
    # int(hight) * int(hight_dot) -> 다음 인덱스
    length = int(hight) * int(hight_dot) + int(weight_dot)
    test_temp_list[length] = 1
    coordinate.append((weight_dot, hight_dot))

# 1. 큐에 넣어서, 해당 bug 가 상하좌우로 계산이 가능한지 확인.
# 2. 0으로 변경
# 3. 상하좌우에 없으면 바로 다음 bug 조회
print(test_temp_list)
queue = []
bug = 0

# 2 (가로), 2 (세로), 1 (심어진 배추의 개수)
# 0, 0
# 0, 1

# 0,0 기준
# 상 -> 0, -1 -> x
# 하 -> 0, 1  -> o -> 2 (index)
# 좌 -> -1, 0 -> x
# 우 -> 1, 0  -> o -> 1 (index)

# 1,0 기준
# 상 -> 1,-1 -> x
# 하 -> 1, 1 -> o -> 3 (index)
# 좌 -> 0, 0 -> o -> 0 (index)
# 우 -> 2, 0 -> x

bug = 0
while 1:
    _weight_dot, _hight_dot = coordinate[0]
    # 이동 순서 상 > 하 > 좌 > 우
    