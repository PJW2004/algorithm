# 테스트 케이스 값을 받고
# N행, M열 값을 전달 받으면,
# M열의 값을 전부 더하고
# 가장 큰 값의 index 값을 갱신한다.
# 값이 같아도 index 값을 갱신한다.
for _ in range(int(input())):
    n, m = map(int, input().split())
    vector = []
    for _ in range(0, m):
        vector.append(list(map(int, input().split())))
    for index, _vector in enumerate(zip(*vector)):
        multiplication = 1
        for _number in _vector:
            multiplication *= _number
        if index == 0:
            lank = 1
            lank_score = multiplication
            continue
        if multiplication >= lank_score:
            lank_score = multiplication
            lank = index+1
    print(lank)