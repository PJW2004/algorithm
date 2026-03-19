# 이 코드는 1% 지나고 시간초과 남.
import sys
import heapq

left_heap = []
right_heap = []

for _ in range(int(sys.stdin.readline())):
    beak_ans = int(sys.stdin.readline())
    
    if len(left_heap) == len(right_heap):
        # python 의 heapq 는 기본적으로 최소힙은 제공하지만,
        # 최대힙은 제공하지 않음.
        heapq.heappush(left_heap, (-beak_ans, beak_ans))
        # 최댓값에 마이너스를 붙이게 되면 최솟값이 되는 원리를 이용.
    else:
        heapq.heappush(right_heap, (beak_ans, beak_ans))
    # ex: 1
    #     left_heap  : [(-1, 1)]
    #     right_heap : []
    
    # 최소힙이 존재하며, 최대힙이 최소힙보다 더 큰 값을 가지는 경우.
    if right_heap and left_heap[0][1] > right_heap[0][0]:
        _min=heapq.heappop(right_heap)[0] # 최소힙의 값이 최대힙의 값이 되어야 하고.
        _max=heapq.heappop(left_heap)[1]  # 최대힙의 값이 최소힙의 값이 되어야 한다.
        # 아래의 과정은 위와 동일하다.
        heapq.heappush(left_heap, (-_min, _min))
        heapq.heappush(right_heap, (_max, _max))

    print(left_heap[0][1])
