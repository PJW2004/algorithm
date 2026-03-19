# 선택 정렬 이로구만.
data = list(map(int, input().split()))
while True:
    # 무조건 5조각
    for index in range(len(data)-1):
        if data[index] > data[index+1]:
            _temp = data[index+1]
            data[index+1] = data[index]
            data[index] = _temp
            print(" ".join(map(str, data)))
    if data == [1,2,3,4,5]:
        break