for _ in range(int(input())):
    score_list = list(map(int, input().split()))
    # 심판은 5명
    # 최고점과 최저점은 처음에 뺀 나머지 3명의 합을 계산
    # 나머지 3명의 최고점과 최저점의 차이의 절대값 (abs) 가 4점 이상이면 "KIN" 출력
    score_list.remove(max(score_list))
    score_list.remove(min(score_list))
    if abs(max(score_list) -min(score_list)) >= 4:
        print("KIN")
    else:
        print(sum(score_list))