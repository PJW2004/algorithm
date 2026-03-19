import sys
n,c = map(int,sys.stdin.readline().split())
# 26% 가다가 시간초과
data = [int(sys.stdin.readline()) for _ in range(n)]
count = 0
# for cycle in range(1, c+1):
    # 2% 가다가 시간초과
    # if 0 in map(lambda y :cycle%y, data):
    #     count += 1
    # 23% 가다가 시간초과
    # if any(cycle % y == 0 for y in data):
    #     count += 1

filtered = [] # 데이터 축소 (57% 이후)
# {2,4,6} -> {2,3} 남기는 커버리지
for y in data:
    if all(y % z != 0 for z in filtered):
        filtered.append(y)
data = filtered

visited = bytearray(c + 1) # 중복을 배제
for y in data: # 에라토스테네스 방식
    for multiple in range(y, c + 1, y):
        # 57% 가다가 시간초과
        visited[multiple] = 1
print(sum(visited[1:]))