# 참고 : https://adjh54.tistory.com/384

# 이번엔 투 포인터로 풀어볼거에요.
# m 이 target 이겠지.
n,m=map(int,input().split())
cards=list(map(int,input().split()))

# 투 포인터 접근을 위해선 정렬이 먼저 되야 한다고 했음.
cards.sort() # ex: [5,6,7,8,9]
best_sum=0

for i in range(n-2): # 최댓값 3을 안넘도록.
    # 이때부터 투포인터로 접근이 가능함.
    # left와 right 라는 두개의 포인터를 배열의 양 끝에서 시작.
    left = i+1
    right = n-1

    # left 가 right 보다 크면 안됨.
    while left < right:
        # 합을 먼저 구하고.
        temp_sum=cards[i] + cards[left] + cards[right]

        if temp_sum == m:
            best_sum = temp_sum
            # 이거보다 더이상 좋은 결과가 없으므로
            # left += 1
            # right -= 1
            break
        elif temp_sum < m:
            best_sum = max(best_sum, temp_sum)
            left += 1
        else:
            right -= 1
print(best_sum)