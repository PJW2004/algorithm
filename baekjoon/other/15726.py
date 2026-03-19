# 세개의 수를 띄어쓰기로 입력받아.
# sorted 를 이용해 정렬하고, 인덱스 0번과 1번을 곱한 값을 -1번으로 나눈 몫을 출력하자.
import sys
numbers:list = list(map(int, sys.stdin.readline().split()))
# 세 수의 순서는 변하지 않는다.
print(max(int(numbers[0]*numbers[1]/numbers[2]),int(numbers[0]/numbers[1]*numbers[2])))