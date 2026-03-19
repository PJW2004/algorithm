# n 과 m 을 입력 받아.
# m 을 넘지 않으면서도 m 과 최대한 가까운 3개의 합을 구해야해.
# n 은 카드의 개수 이며 3개 이상 100개 이하가 주어져.

# 브루트 포스 알고리즘으로 풀게 되면.
# 조합 공식으로 100_C_3 이겠네.
# 최대 161,700 번 순회 하겠네.
# 가능한 모든 조합 이므로, 슬라이딩 윈도우와는 다르겠구나.
# 그러면 브루트 포스로 순회하기 위해 3중 for 문으로 접근해볼까.
n,m=map(int,input().split())
cards=list(map(int,input().split()))
max_sum=0
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1, n):
            # print(f'{i} {j} {k}')
            current_sum = cards[i] + cards[j] + cards[k]
            if current_sum <= m and current_sum > max_sum:
                max_sum = current_sum
print(max_sum)