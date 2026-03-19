import sys
sys.setrecursionlimit(10_000)
N = int(input())
T_list = list(map(int, sys.stdin.readline().split()))
T, P = map(int, sys.stdin.readline().split())

# 첫 줄에 티셔츠를 T장씩 최소 몇 묶음 주문해야 하는지 출력하세요.
cnt = 0
for _t in T_list:
    if not _t:
        continue
    if (_t // T) == 0:
        cnt += 1
    elif (_t // T) != 0 and (_t % T) == 0:
        cnt += _t // T
    elif (_t // T) != 0 and (_t % T) > 0:
        cnt += (_t // T) + 1
# 다음 줄에 펜을 P자루씩 최대 몇 묶음 주문할 수 있는지와, 
# 그 때 펜을 한 자루씩 몇 개 주문하는지 구하세요.
lst = [N // P, N % P]

print(cnt)
print(*lst)