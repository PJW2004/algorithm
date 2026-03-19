# 먼저 몇번 과정을 반복할 것인지 입력 받는다.
# 그리고, 입력의 테스트 케이스 첫 줄에는 아이의 인원을 입력 받는다.
# 다음 줄에는 각 아이의 인원마다 몇개의 사탕을 가지고 있는지 입력 받는다.
# 홀수 개의 아이에게는 먼저 선생님이라는 객체가 아이에게 1개의 사탕을 준다.
# 다음으로, 각각 옆에 있는 아이에게 자신이 가지고 있는 사탕의 절반을 준다.
# 이게 1순환.
# 예시)
# 2 4 7 8 9      (처음 상태)               
# 2 4 8 8 10     (선생 사탕 줌) - 0순환
# 6 3 6 8 9      (옆에 사탕 줌) 
# 6 4 6 8 10     (선생 사탕 줌) - 1순환
# 8 5 5 7 9      (옆에 사탕 줌) 
# 8 6 6 8 10     (선생 사탕 줌) - 2순환
# 9 7 6 7 9      (옆에 사탕 줌) 
# 10 8 6 8 10    (선생 사탕 줌) - 3순환
# 10 9 7 7 9     (옆에 사탕 줌) 
# 10 10 8 8 10   (선생 사탕 줌) - 4순환
# 10 10 9 8 9    (옆에 사탕 줌) 
# 10 10 10 8 10  (선생 사탕 줌) - 5순환
# 10 10 10 9 9   (옆에 사탕 줌) 
# 10 10 10 10 10 (선생 사탕 줌) - 6순환
# 그러면 한 아이만 있는경우에는 그냥 0순환 이겠네.

"""
문제 풀고, 다른 사람 푼것까지 확인한게. 
39분 걸림.
"""
import sys
for _ in range(int(sys.stdin.readline())):
    children = int(sys.stdin.readline())
    candies = list(map(int, sys.stdin.readline().split()))
    if children == 1:
        print(0)
        continue
    count = 0
    while 1:
        # 1. 선생 사탕 줌.
        candies = [candy + 1 if candy % 2 else candy for candy in candies]
        if all(candies[index] == candies[0] for index in range(1, children)):
            # 모두 동일해 지면 순환 종료
            break
        # 2. 옆에 사탕 줌.
        change_candies = [candies[index]//2 + candies[index-1]//2 for index in range(children)]
        count += 1
        candies = change_candies
    print(count)