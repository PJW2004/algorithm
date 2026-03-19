# 최대 5번 이동, 매번 4방향
# -> 4^5 = 1,024가지
# 모든 경우를 빠짐없이 탐색
# -> DFS(깊이 우선 탐색)로 재귀
# 각 이동을 실제로 수행
# -> 2048 게임 규칙 시뮬레이션

import sys
from copy import deepcopy

input = sys.stdin.readline

def move(board, direction):
    # 왼쪽으로 밀기만 구현
    # 다른 방향은 보드를 회전시켜서 왼쪽으로 민 뒤 다시 복원
    n = len(board)
    b = deepcopy(board)

    def rotate_90(b):
        # 시계 방향 90도 회전
        return [list(row) for row in zip(*b[::-1])]
    
    def rotate_270(b):
        # 반시계 방향 90도 회전 (= 시계 270도)
        return [list(row) for row in zip(*b)][::-1]
    
    def rotate_180(b):
        # 180도 회전
        return [row[::-1] for row in b[::-1]]
    
    # 방향에 따라 보드를 회전해서 "항상 왼쪽으로 미는 문제"로 변환
    if direction == 0:
        # 위
        b = rotate_90(b)
    elif direction == 1:
        # 아래
        b = rotate_270(b)
    elif direction == 2:
        # 왼쪽
        pass
    elif direction == 3:
        # 오른쪽
        b = rotate_180(b)

    # 왼쪽으로 밀기
    for row in range(n):
        # 0이 아닌 블록만 추출 (빈칸 제거)
        # 예: [0,2,0,2] > [2,2]
        blocks = [x for x in b[row] if x != 0]

        # 앞에서부터 인접한 같은 값 합치기
        # 예: [2,2] > [4,0] (한 번 합쳐진 자리는 스킵)
        merged = []
        skip = False
        for i in range(len(blocks)):
            if skip:
                skip = False
                continue
            # 다음 블록과 값이 같으면 합치기
            if i + 1 < len(blocks) and blocks[i] == blocks[i+1]:
                merged.append(blocks[i] * 2) # 합쳐진 값
                skip = True # 다음 블록은 이미 합쳐졌으므로 건너뜀
            else:
                merged.append(blocks[i])
        
        # 나머지를 0으로 채워서 길이 n 맞추기
        # 예: [4] > [4,0,0,0]
        merged += [0] * (n - len(merged))
        b[row] = merged
    
    # 다시 원래 방향으로 복원
    if direction == 0:
        # 위
        b = rotate_270(b)
    elif direction == 1:
        # 아래
        b = rotate_90(b)
    elif direction == 2:
        # 왼쪽
        pass
    elif direction == 3:
        # 오른쪽
        b = rotate_180(b)

    return b

# DFS 로 모든 경우 깊이 우선 탐색
answer = 0 # 전역 최대값

def dfs(board, depth):
    # 현재 board 상태에서 depth번 이동한 상태.
    # depth가 5에 도달하면 최대 블록을 확인.
    # 아니면 4방향 각각으로 이동하여 재귀 호출.
    global answer

    # 5번 이동 완료
    if depth == 5:
        # 보드에서 가장 큰 값을 찾아 최대값 갱신
        max_block = max(max(row) for row in board)
        answer = max(answer, max_block)
        return
    
    # 4방향 각각 시도
    # 방향:
    # -> 0=위
    # -> 1=아래
    # -> 2=왼쪽
    # -> 3=오른쪽
    for direction in range(4):
        # 이 방향으로 이동한 새 보드를 만들고
        new_board = move(board, direction)
        # 한 단계 더 깊이 탐색
        dfs(new_board, depth + 1)
        # 재귀가 끝나면 자동으로 백트래킹

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 깊이 0에서 출발
dfs(board, 0)

print(answer)