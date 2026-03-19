# 여기서 나머지는 초
# print(4263//3600) # 시
# print((4263%3600)//60) # 분
# print(4263%60) # 초

# 86400 이 24시면 0 0 1 이 반환 되어야해.
# print(24*3600)
# print(86400//3600) # 시

# 초기화된 시간을 가져오고.
# 이 시간을 초로 변환
# ex) 0 1 0 -> 0*3600 + 1*60 + 0 = 60

# 몇번 할건지 입력 받고
#   -> T 가 1일때 c 입력 초 +
#   -> T 가 2일때 c 입력 초 -
#   -> T 가 3일때 출력에 맞게 변환후 출력
import sys
hour,minute,second = map(int, sys.stdin.readline().split())
init_second = hour*3600 + minute*60 + second
for _ in range(int(sys.stdin.readline())):
    input_list = list(map(int, sys.stdin.readline().split()))
    match input_list[0]:
        case 1:
            init_second = (init_second + input_list[1]) % 86400
        case 2:
            init_second = (init_second - input_list[1]) % 86400
        case 3:
            print(f'{init_second//3600} {(init_second%3600)//60} {init_second%60}')