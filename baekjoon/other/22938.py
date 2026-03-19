import sys

# 입력을 빠르게 받기 위한 설정
input = sys.stdin.readline

# 첫 번째 원의 정보 입력
x1, y1, r1 = map(int, input().split())

# 두 번째 원의 정보 입력
x2, y2, r2 = map(int, input().split())

# 두 원의 중심 사이의 거리의 제곱 계산
# (x2 - x1)^2 + (y2 - y1)^2
d_squared = (x1 - x2)**2 + (y1 - y2)**2

# 두 원의 반지름의 합의 제곱 계산
# (r1 + r2)^2
r_sum_squared = (r1 + r2)**2

# 조건 비교 후 결과 출력
if d_squared < r_sum_squared:
    print("YES")
else:
    print("NO")