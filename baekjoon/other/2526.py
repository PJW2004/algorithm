initation_number, p = map(int, input().split())
cycle = []
current = initation_number
first_index = -1
while True:
    # 예)
    # initation_number : 67
    # p : 3
    # (67 * 67) % 31 = 25
    # (25 * 67) % 31 = 1
    # (1 * 67) % 31 = 5
    # (5 * 67) % 31 = 25 (반복 시작)
    # 따라서 Cucle length = 3
    current = (current * initation_number) % p
    if current in cycle:
        first_index = cycle.index(current)
        break
    cycle.append(current)
# 시작 지점에서 부터 계산이 되었어야 했어.
print(len(cycle) - first_index)