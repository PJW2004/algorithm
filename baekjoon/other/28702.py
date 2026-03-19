# 주어진 수열의 항들로부터 공차(common difference) 를 유도하고, 이를 통해 다음 항을 예측.
# -> 등차수열 문제.
# 연속으로 세개의 문자열의 출력이 주어짐.
# -> 각 문자열의 길이는 8이하.
import sys
fizz_buzz_data:list[str] = []
for _ in range(3):
    fizz_buzz_data.append(sys.stdin.readline().strip())

# 1번 공식 적용.
k = 1 # 기준점 위치
v_k = 0 # 기준점 값
for index, data in enumerate(fizz_buzz_data):
    if data.isdecimal():
        k = index + 1
        v_k = int(data)
        break
a_4 = v_k + 4 - k

# 2번 FizzBuzz 규칙 적용.
if (a_4 % 3 == 0) and (a_4 % 5 == 0):
    print('FizzBuzz')
elif (a_4 % 3 == 0) and (a_4 % 5 != 0):
    print('Fizz')
elif (a_4 % 3 != 0) and (a_4 % 5 == 0):
    print('Buzz')
else:
    print(a_4)