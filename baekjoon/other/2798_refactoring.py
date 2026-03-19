n, m = map(int, input().split())
cards = list(map(int, input().split()))

# 먼저 카드를 정렬한다.
cards.sort()

max_sum = 0
for i in range(n - 2):
    # [가지치기 1] 
    # 현재 카드(i)가 m보다 크면, 이후의 조합은 절대 m을 넘지 못하므로 종료.
    # 단, cards[i] + cards[i+1] + cards[i+2] > m 으로 더 정교하게 할 수도 있음.
    if cards[i] > m:
        break
        
    for j in range(i + 1, n - 1):
        # [가지치기 2]
        # 두 카드의 합이 이미 m보다 크면, 가장 작은 세 번째 카드를 더해도 m을 넘으므로 스킵.
        if cards[i] + cards[j] > m:
            break
            
        for k in range(j + 1, n):
            current_sum = cards[i] + cards[j] + cards[k]
            
            # [가지치기 3]
            # 세 카드의 합이 m을 초과하면, 더 큰 k를 더해볼 필요가 없으므로 k 루프 탈출.
            if current_sum > m:
                break
            
            # 합이 m 이하인 경우에만, 최대값 갱신을 시도.
            if current_sum > max_sum:
                max_sum = current_sum
                
print(max_sum)