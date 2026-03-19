# 퀸은 상 하 좌 우 / 대각선 이동이 가능.
N = int(input())

# [[1, 1, 1, 1, 1, 1, 1, 1], 
#  [1, 1, 0, 0, 0, 0, 0, 0], 
#  [1, 0, 1, 0, 0, 0, 0, 0], 
#  [1, 0, 0, 1, 0, 0, 0, 0], 
#  [1, 0, 0, 0, 1, 0, 0, 0], 
#  [1, 0, 0, 0, 0, 1, 0, 0], 
#  [1, 0, 0, 0, 0, 0, 1, 0], 
#  [1, 0, 0, 0, 0, 0, 0, 1]]

# [[1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 0, 0, 0, 0, 0, 0],
#  [1, 0, 1, 0, 0, 0, 0, 0],
#  [1, 0, 0, 1, 0, 0, 0, 0],
#  [1, 0, 0, 0, 1, 0, 0, 0],
#  [1, 0, 0, 0, 0, 1, 0, 0],
#  [1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 0, 0, 0, 0, 0, 0, 1]]

def generate_queen_table(y, x, N):
    table = [[0] * N for _ in range(N)]
    
    for i in range(N):
        table[y][i] = 1  # 가로
        table[i][x] = 1  # 세로

    # 대각선
    for dy in [-1, 1]:
        for dx in [-1, 1]:
            ny, nx = y + dy, x + dx
            while 0 <= ny < N and 0 <= nx < N:
                table[ny][nx] = 1
                ny += dy
                nx += dx

    table[y][x] = 0  # 자기 자신은 0으로
    return table

# 모든 위치에 대해 테이블 생성
table_list = []
for y in range(N):
    for x in range(N):
        table_list.append(generate_queen_table(y, x, N))

# 예시 출력: (0, 0)에 퀸이 있을 때의 공격 위치
from pprint import pprint
pprint(table_list)
