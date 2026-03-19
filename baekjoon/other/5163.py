# 첫 줄에 데이터의 수 K
import math
for index in range(1, int(input())+1):
    # 첫 줄에 정수 b와 소수 w가 주어집니다. 
    # b >= 0인 b는 푸가 사용하는 풍선의 수이며, 
    # w는 (g으로 나타낸) 푸의 무게입니다.
    ballon_count, bear_gram = input().split()
    bear_gram = float(bear_gram)
    ballon_connect = 0.0
    for _ in range(int(ballon_count)):
        # 이후 b개의 줄 각각에 하나의 소수 ri >= 0이 입력됩니다. 
        # 이는 (cm로 나타낸) i번째 풍선의 반지름의 길이입니다.
        radius_length = float(input())

        # 풍선은 완전 구형
        # 풍선 자체의 무게와 줄의 무게는 무시
        # 부력과 관련해 당신이 알아야 하는 정보
        # - 1L의 헬륨 (1000cm3)은 1g의 무게를 들어 올릴 수 있습니다. 
        # - 반지름이 r인 구의 부피는 4/3πr3입니다. 
        #   (입력에 부력이 무게를 정확히 상쇄하는 "평형" 상태는 주어지지 않습니다. 
        #   반올림 관련 문제를 피하기 위해, 
        #   부력이 무게를 띄우기 위해 필요한 크기보다 최소 0.001만큼 부족하거나 넘침 역시 보장됩니다.)
        volume_cm3:float = 4/3 * math.pi * (radius_length**3)
        ballon_connect += volume_cm3 / 1000
    print(f"Data Set {index}:")
    if ballon_connect >= bear_gram:
        print("Yes")
    else:
        print("No")
    del ballon_connect, bear_gram
    print()