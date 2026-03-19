# 이 코드는 1% 지나고 시간초과 남.
import sys
numbers = []
for _ in range(int(sys.stdin.readline())):
    beak_ans = int(sys.stdin.readline())
    numbers.append(beak_ans)
    sorted_numbers = sorted(numbers)
    # 리스트의 크기를 먼저 구하고.
    # - 홀수면 2를 나눈 몫으로 접근하자.
    # - 짝수면 2를 나눈 몫에 1을 빼서 접근하자.
    length = len(sorted_numbers)
    if length % 2 == 0: # 짝수 / 홀수
        print(sorted_numbers[length//2-1])
    else:
        print(sorted_numbers[length//2])