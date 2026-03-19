# 최빈값은 count 로 하면 되겠네.
number_list = []
number_count = [[0,0]] # 더미 데이터
for _ in range(0,10): # 10번
    number = int(input())
    number_list.append(number)
    for index,number_info in enumerate(number_count):
        if number_info[0] == number:
            number_info[-1] += 1
            break
    else:
        number_count.append([number,1])
print(sum(number_list) // 10) # 평균
number_count = [(_count,_number) for _number,_count in number_count[1:]] # 더미데이터 지우고.
print(sorted(number_count, reverse=True)[0][-1]) # 최빈값