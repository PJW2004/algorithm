# 브루트 포스 알고리즘.
# -> 해가 존재할 것으로 예상되는 모든 영역을 전체 탐색하는 방법

# 남는 사탕은 없어야 한다.
# 남규는 영훈이보다 2개 이상 많은 사탕을 가져야 한다.
# 셋 중 사탕을 0개 받는 사람은 없어야 한다.
# 택희가 받는 사탕의 수는 홀수개가 되어서는 안 된다.
candy=int(input())
# 택희(짝수), 남규(영훈 보다 2개 이상), 영훈 (1개 이상)
count = 0
for a,b,c in [(a,b,c) for a in range(candy) for b in range(candy) for c in range(candy)]:
    if (a % 2 == 0) and (a != 0) and (b + 2 <= c) and (b > 0) and (a + b + c == candy):
        count += 1
print(count)